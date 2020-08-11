from django.contrib import admin

from assessments.datatests.models import Question, Answer


class AnswersInLine(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswersInLine]


admin.site.register(Question, QuestionAdmin)
