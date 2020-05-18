from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import  QuestionView, QuestionDetailView,UserQuestionDetailView

urlpatterns = [
    path('question/all/', QuestionView.as_view()),
    path('question/<int:pk>/', QuestionDetailView.as_view()),
    path('question/user/<int:user_id>/', UserQuestionDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)