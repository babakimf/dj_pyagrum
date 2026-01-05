import pyagrum as gum 
from django.apps import apps

def run_diagnosis(form, target = 'Parent'):
    bn = apps.get_app_config('disease').bn_model
    
    evidence = {}
    for field in form.cleaned_data:
        value = form.cleaned_data[field]
        if value:
            evidence[field.capitalize()] = value
              
    ie = gum.LazyPropagation(bn)
    ie.setEvidence(evidence)
    ie.makeInference()
    post = ie.posterior(target)           
    
    post = post.topandas()
    post.index = post.index.droplevel(0)
    no = round(float(post["No"]), 3)
    yes = round(float(post["Yes"]), 3)
    post_str = f'{target} posterior probability: No = {no}, Yes = {yes}'
    return post_str