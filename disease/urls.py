from django.urls import path 
from django.views.generic import TemplateView

urlpatterns = [
    path("diagnosis/", TemplateView.as_view(template_name = "diagnosis.html"), name = 'diagnosis'),
]
