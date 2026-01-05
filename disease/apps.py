from django.apps import AppConfig
import pyagrum as gum

class DiseaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "disease"
    bn_model = None
    
    def ready(self):
        DiseaseConfig.bn_model = gum.loadBN("disease/model/SimpleBN.bif")
