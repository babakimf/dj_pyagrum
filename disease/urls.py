from django.urls import path 
from .views import DiagnosisCreateView, DiagnosisDetailView

urlpatterns = [
    path("", DiagnosisCreateView.as_view(), name = 'diagnosis'),
    path("diagnosis_detail/<int:pk>", DiagnosisDetailView.as_view(), name = 'diagnosis_detail'),
]
