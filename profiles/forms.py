from django import forms

from .models import form_file_upload


class profile_forms(forms.Form):

    
    form_file = forms.FileField(allow_empty_file=False)
    from_image = forms.ImageField(allow_empty_file=False)

    # class Meta :
        
    #     model = form_file_upload
    #     fields = '__all__' 
    #     labels = {
    #         'model_file':"attach formal files",
    #         'model_image' : "attach only image file"
    #     }