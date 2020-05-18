from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import  EducationTypeView, EducationTypeDetailView,InstitutionView,InstitutionDetailView,BoardView,BoardDetailView,EducationDetailView,UserEducationDetailView

urlpatterns = [
    path('education-type/', EducationTypeView.as_view()),
    path('education-type/<int:pk>/', EducationTypeDetailView.as_view()),
    path('institution/', InstitutionView.as_view()),
    path('institution/<int:pk>/', InstitutionDetailView.as_view()),
    path('board/', BoardView.as_view()),
    path('board/<int:pk>/', BoardDetailView.as_view()),
    path('education-detail/', EducationDetailView.as_view()),
    path('education-detail/user/<int:user_id>/', UserEducationDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)