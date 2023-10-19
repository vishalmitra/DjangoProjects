from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import profile_forms
from .models import form_file_upload
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.
def store_static(file):
   
    with open(f"temp/{file.name}.jpg","wb+") as destionation:
        for chunk in file.chunks() :
            destionation.write(chunk)       
    pass

class Create_view_for_upload(CreateView):
    template_name ="profiles/create_profile.html"
    model= form_file_upload
    
    fields = "__all__"
   
    success_url= "/profiles"

class List_view_table(ListView ):
    template_name ="profiles\list_view.html"
    model = form_file_upload


class CreateProfileView(View):
    def get(self, request):
        file = profile_forms()
        return render(request, "profiles/create_profile.html",{'file':file})
    

    def post(self, request):
        # we use the  "image" because name = image in the html tag input = file tag 
        file = profile_forms(request.POST,request.FILES )
       
        print(request.FILES)
        if file.is_valid():

            data_base_table_object = form_file_upload(model_file=request.FILES['form_file'],
                 model_image=request.FILES['from_image'])

            data_base_table_object.save()

            # file = request.FILES["image"] is used when input is taking from html input tag 
            # as input type is file
                #print( f"file type is  {file.content_type}" )
                #print( f" file size is  {file.size} ")          
            #store_static(request.FILES['form_file'])
            #these content_type ,name, size other  inbulit functions were can check in the uploads in the documentation
            return HttpResponseRedirect("/profiles")
       
        return render(request,"profiles/create_profile.html",{"file":file})
        
