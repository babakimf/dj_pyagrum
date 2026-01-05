from django.shortcuts import render
from django.urls import reverse_lazy
from django.apps import apps
from django.views.generic import CreateView, DetailView
import pyagrum as gum
from .forms import EvidenceForm
from .models import Evidence 
from .diagnosis import run_diagnosis
# Create your views here.

class DiagnosisCreateView(CreateView):
    model = Evidence 
    form_class = EvidenceForm 
    template_name = 'diagnosis.html'
    
    def form_valid(self, form):
       
        post_str = run_diagnosis(form)
        self.object = form.save(commit=False)
        self.object.diagnosis = post_str  # or format nicely
        self.object.save()
        return render(self.request, self.template_name, context={'form':form, 'diagnosis':self.object})
    

class DiagnosisDetailView(DetailView):
    model = Evidence 
    template_name = 'diagnosis_detail.html'
    context_object_name = 'diagnosis'
    

    
    
    