from django.db import models 
from django.urls import reverse

THREE_OPTIONS = [('None', 'None'), ('Low', 'Low'), ('High', 'High')]
TWO_OPTIONS = [('No','No'), ('Yes', 'Yes')]
class Evidence(models.Model):
    child1 = models.CharField("Child 1", max_length=10, choices = THREE_OPTIONS, null=True, blank = True)
    child2 = models.CharField('Child 2', max_length=10, choices = TWO_OPTIONS, null=True, blank = True)
    diagnosis = models.CharField('Diagnosis: ', max_length=255, null = True, blank = True)
    
    def __str__(self):
        return f"Child 1: {self.child1}, Child 2: {self.child2}, Diagnosis: {self.diagnosis}" 
    
    def get_absolute_url(self):
        return reverse("diagnosis_detail", kwargs={"pk": self.pk})
    