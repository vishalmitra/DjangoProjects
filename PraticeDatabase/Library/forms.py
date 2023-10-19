from django import forms
from .models import  forms_django



"""
class myform(forms.Form):

    username = forms.CharField(max_length=15,error_messages={"name":"should not exceed 15 charecters"})                                                           
    email=forms.EmailField()
    review =forms.CharField(widget=forms.Textarea,max_length=100)
    # gender =forms.RadioSelect()
"""

class myform (forms.ModelForm):
    class Meta:
        # here we are giving 'model variable'  is assiged to model 'forms_django'  that already created in models.py
        # so we can connect to that exists model to forms_django with forms.py class myform
        # forms_django is model <== data in comming  ==>  myform(ModelForm)
        # as per understanding  model,fields,lables needed to be same 

        model = forms_django
        # exclude =["colum or field"] can mention colums in models that are need to not show in template
        fields = '__all__' # this tells django all the fields are included to take data input
        
        # values are exact variables on the left are in  model in models.py to that we are 
        # giving new lables to show on html template 
        labels ={'username':" your username",  
                 'email' : " Your email",
                 "review":" Your review"                
                }        
        
        error_messages = {
            "username":{'required':"name should not be empty", "max_length":"should execed more than 15 chars"}             
                        
                        }
        






