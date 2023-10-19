from django.db import models

# Create your models here.1


class form_file_upload (models.Model):
    #this upload_to  look for project level path to store it 
    #may be this data and images that i give in upload_to is same name like data,images
    #as per my inderstanding because after giving images its shows i need to pip pillow
    model_file = models.FileField(upload_to='data')
    model_image =models.ImageField(upload_to ="images",null=True)
