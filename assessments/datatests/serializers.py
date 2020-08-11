from rest_framework import serializers

from assessments.datatests.models import Question, Answer, QuestionAndAnswer, Assessment


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'id']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['body', 'answers', 'id']
        depth = 1


class QuestionAndAnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    selected_answer = AnswerSerializer(read_only=True)

    class Meta:
        model = QuestionAndAnswer
        fields = ['question', 'selected_answer', 'assessment']


class AssessmentSerializer(serializers.ModelSerializer):
    questions_and_answers = QuestionAndAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = ['questions_and_answers']
