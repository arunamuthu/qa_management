from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import  AnswerView,AnswerDetailView,UserAnswerDetailView,QuestionAnswerDetailView,UpvoteView,UpvoteDetailView,DownvoteView,DownvoteDetailView,AnswerUpvoteView,AnswerDownvoteView

urlpatterns = [
    path('answer/all/', AnswerView.as_view()),
    path('answer/<int:pk>/', AnswerDetailView.as_view()),
    path('answer/user/<int:user_id>/', UserAnswerDetailView.as_view()),
    path('answer/question/<int:question_id>/', QuestionAnswerDetailView.as_view()),
    path('user/<int:user_id>/upvote/', UpvoteView.as_view()),
    path('user/<int:user_id>/upvote/<int:pk>/', UpvoteDetailView.as_view()),
    path('user/<int:user_id>/downvote/', DownvoteView.as_view()),
    path('user/<int:user_id>/downvote/<int:pk>/', DownvoteDetailView.as_view()),
    path('user/upvote/<int:answer_id>/', AnswerUpvoteView.as_view()),
    path('user/downvote/<int:answer_id>/', AnswerDownvoteView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)