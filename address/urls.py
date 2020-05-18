from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  StateView,StateDetailView,CityView,CityDetailView,AddressView,AddressDetailView

urlpatterns = [
    path('state/', StateView.as_view()),
    path('state/<int:pk>/', StateDetailView.as_view()),
    path('state/<int:state_id>/city/', CityView.as_view()),
    path('state/<int:state_id>/city/<int:pk>/', CityDetailView.as_view()),
    path('address/', AddressView.as_view()),
    path('address/<int:user_id>/', AddressDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)