from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import  SkillSetView,SkillSetDetailView,AreaOfInterestView,UserAreaOfInterestView

urlpatterns = [
    path('skill/', SkillSetView.as_view()),
    path('skill/<int:pk>/', SkillSetDetailView.as_view()),
    path('area-of-interest/', AreaOfInterestView.as_view()),
    path('area-of-interest/<int:user_id>/', UserAreaOfInterestView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)