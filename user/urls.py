from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  ProfileView,ProfileDetailView,UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('user/', ProfileView.as_view()),
    path('user/<int:pk>/', ProfileDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)