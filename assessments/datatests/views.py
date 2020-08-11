import random

from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.utils.timezone import now
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from assessments.datatests.models import Question, Assessment, QuestionAndAnswer, User, Answer
from assessments.datatests.serializers import QuestionSerializer, QuestionAndAnswerSerializer, AssessmentSerializer
from assessments.datatests.utils import response


ASSESSMENT_MINUTES = 60


class CreateAssessment(APIView):
    """
    Creates user and assessment
    """
    def post(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('next-question'))
        request_data = request.data
        email = request_data.get('email')
        first_name = request_data.get('first_name')
        last_name = request_data.get('last_name')

        if email and first_name and last_name:
            user = User.objects.filter(email=email).first()
            if not user:
                user = User(email=email, first_name=first_name, last_name=last_name)
                user.save()
            login(request, user)
            assessment = Assessment(user=user)
            assessment.save()
            return redirect(reverse('next-question'))
        else:
            message = "All fields, email, first_name and last_name are required"
        return response({}, message=message)


class SaveAnswer(APIView):
    """
    Saves answer for the current assessment
    """
    def post(self, request):
        if request.user.is_authenticated:
            request_data = request.data
            question_id = request_data.get('question_id')
            answer_id = request_data.get('answer_id')
            if not question_id:
                return response("question_id is required")

            assessment = Assessment.objects.filter(
                user=request.user,
                submitted_date__isnull=True
            ).order_by('-start_date').first()

            question_and_answer = QuestionAndAnswer.objects.filter(
                assessment=assessment,
                question_id=question_id
            ).first()

            answer = Answer.objects.filter(id=answer_id).first() if answer_id else None

            if question_and_answer:
                question_and_answer.selected_answer = answer
                question_and_answer.save()
            else:
                question_and_answer = QuestionAndAnswer(
                    assessment=assessment,
                    question=Question.objects.get(id=question_id),
                    selected_answer=answer,
                    number=QuestionAndAnswer.objects.filter(assessment=assessment).count() + 1
                )
                question_and_answer.save()
            return response(QuestionAndAnswerSerializer(question_and_answer).data, message='success')


class QuestionDetail(APIView):
    """
    Retrieves next question
    """
    def get(self, request):
        if request.user.is_authenticated:
            assessment = Assessment.objects.filter(
                user=request.user,
                submitted_date__isnull=True
            ).order_by('-start_date').first()

            estimated_end_date = assessment.estimated_end_date
            message = None
            serializer = None
            now_date = now()
            if estimated_end_date < now_date:
                return response({}, "Time ended")
            elif assessment:
                questions_and_answers = QuestionAndAnswer.objects.filter(assessment=assessment)
                pending_questions = Question.objects.all().exclude(
                    id__in=[q_a_a.question.id for q_a_a in questions_and_answers]
                )
                if not pending_questions:
                    return redirect(reverse('check-assessment'))
                else:
                    question = random.choice(pending_questions)
                    serializer = QuestionSerializer(question)
            return response(
                {
                    'data': serializer.data if serializer else None,
                    'remaining_time': int(ASSESSMENT_MINUTES - ((now_date - assessment.start_date).total_seconds() / 60))
                },
                message=message
            )
        return response({}, "No user authenticated")


class CheckAssessment(APIView):
    """
    Retrieves the current assessment status
    """
    def get(self, request):
        if request.user.is_authenticated:
            assessment = Assessment.objects.filter(
                user=request.user,
                submitted_date__isnull=True
            ).order_by('-start_date').first()
            return response(
                {
                    "data": AssessmentSerializer(assessment).data,
                    'remaining_time': int(
                        ASSESSMENT_MINUTES - ((now() - assessment.start_date).total_seconds() / 60))
                },
                "success"
            )
        return response({}, "No user authenticated")


class SubmitAssessment(APIView):
    """
    Ends the current assessment
    """
    def post(self, request):
        if request.user.is_authenticated:
            assessment = Assessment.objects.filter(
                user=request.user,
                submitted_date__isnull=True
            ).order_by('-start_date').first()
            assessment.submitted_date = now()
            assessment.save()
            logout(request)
            return response({}, "submitted successfully")
        return response({}, "No user authenticated")
