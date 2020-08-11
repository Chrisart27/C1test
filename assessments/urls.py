"""assessments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from assessments.datatests import views

urlpatterns = [
    path('assessment/save', views.SaveAnswer.as_view(), name='save-question'),
    path('assessment/next', views.QuestionDetail.as_view(), name='next-question'),
    path('assessment/check', views.CheckAssessment.as_view(), name='check-assessment'),
    path('assessment/start', views.CreateAssessment.as_view(), name='start-assessment'),
    path('assessment/end', views.SubmitAssessment.as_view(), name='end-assessment'),
    path('admin/', admin.site.urls),
]
