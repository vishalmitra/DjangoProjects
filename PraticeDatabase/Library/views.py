from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import myform
from django.core.mail import send_mail
from .models import forms_django,Books
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView,CreateView
#from .forms import 
# Create your views here.

class form_view(FormView):
    form_class   =  myform
    template_name   =   "Library/home.html"
    success_url  =  "thankyou"  #onsucessfull validation for is_validate redirects to this page

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()                                                                                                                         
        return super().form_valid(form)
    
class create_view(CreateView):
    # in create view rather than  over writing any in method  to get stored in database table we will
    # use model property in the create view
    model =  forms_django
    form_class   =  myform
    template_name   =   "Library/home.html"
    success_url  =  "thankyou"  #onsucessfull validation for is_validate redirects to this page



class view_class(View):
    """"""
    def get(self,request):
        form = myform()
        print("checking for the control class view ")

        """ print(f"{request.POST['user_name']}")
                if request.POST["user_name"].isdigit()== True:
                return render(request,"Library/home.html",{"wrong":True})
                this is the like not in built way of validation of forms
            
        """    
        return render( request,"Library/home.html",{"form":form})
        pass


    def post(self,request):
        form = myform(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data))
            #( this form.cleaned_data gives dictionary )
            sorurce_mail ="vishalmithra7@gmail.com"
            mess,email= str(form.cleaned_data['review']), str(form.cleaned_data['email'])

            #database model insertion  normal model created in models.py but advance form base to database 
            #  one is to create Modelform  in forms.py 
            # to avoid the below code 
            """model_let = forms_django(
            username =form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            review =form.cleaned_data['review']
                     
            )          
            """

            """
            here i did a mistake that rather than using  form = myform(request.POST)  to be saved 
            i have created new instance form the model like we use to do for manually do method that  we use 
            to store data using cleaned data['column'] however i solved using chat gpt
            """
            myinstance = form.save()
            #model_let = forms_django()
            #model_let.save()
            print(mess,email)
            #while trying the below line we are getting connection refused error port something 
            #send_mail(subject="katre",message=mess,from_email=sorurce_mail,recipient_list=[email])
            return HttpResponseRedirect("thankyou")
        
        
        pass





def forms_home(request):
    pass 
    print("test for control")
    # this no longer works because we have created a class view for this its on the top as view_class(View)

    if request.method == 'POST':
        # myform is class in forms.py
        form = myform(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data))
            #( this form.cleaned_data gives dictionary )
            sorurce_mail ="vishalmithra7@gmail.com"
            mess,email= str(form.cleaned_data['review']), str(form.cleaned_data['email'])

            #database model insertion  normal model created in models.py but advance form base to database 
            #  one is to create Modelform  in forms.py 
            # to avoid the below code 
            """model_let = forms_django(
            username =form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            review =form.cleaned_data['review']
                     
            )          
            """

            """
            here i did a mistake that rather than using  form = myform(request.POST)  to be saved 
            i have created new instance form the model like we use to do for manually do method that  we use 
            to store data using cleaned data['column'] however i solved using chat gpt
            """
            myinstance = form.save()
            #model_let = forms_django()
            #model_let.save()
            print(mess,email)
            #while trying the below line we are getting connection refused error port something 
            #send_mail(subject="katre",message=mess,from_email=sorurce_mail,recipient_list=[email])
            return HttpResponseRedirect("thankyou")

    else:   
        form = myform()

        """ print(f"{request.POST['user_name']}")
                if request.POST["user_name"].isdigit()== True:
                return render(request,"Library/home.html",{"wrong":True})
                this is the like not in built way of validation of forms
            
        """

    #return HttpResponse("hello world")
    return render( request,"Library/home.html",{"form":form})


#template view had been added insted of rendering function
class Thank_you(TemplateView):
    template_name = "Library/thankyou.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        dic =super().get_context_data(**kwargs)
        #this dic variable is the dictionary  and this method is what we are overloading here 
        dic['message']="thank you this is from get context data overloading method"
        # here we are passing only dict varialble but in the html we are giving only the key of the 
        #dictionary this is somthing odd but python way is to give dict["key"]
        #any way we need to return original dict only here
        return dic



class Reviews_List(ListView):

    template_name ="Library/List_all_reviews.html"

    model=  forms_django

    # we use context_object_name proterty to use the defaut name that we like to iterate in the html
    # page instead of using object_list
    context_object_name = "Total_books"



    #the below function is used to get the filtered data from the table otherwise the by default it 
    #gives the whole list of the data rows from the table
    #if we want the whole list then comment the get_queryset() not overrinding the method  
    
    
    """def get_queryset(self) -> QuerySet[Any]:
        base_query =super().get_queryset()
        filtered_data =base_query.filter(username="user2")
        return filtered_data"""

    """ def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
            dic =super().get_context_data(**kwargs)
            model = forms_django.objects.all()
            dic["model_key"]=model
            return dic
    """

class single_review_page(TemplateView):
    template_name = "Library/single_view_review_page.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        dic =super().get_context_data(**kwargs)
        #this kwargs is like dictionary and id is key we are sending from the url.py as <int:id>

        get_id = kwargs['id']

        # Books is the model name we are imported in header section from models.py 
        selected_review =Books.objects.get(pk=get_id)
        dic["model_key"]= selected_review
        return dic 



class view_detail(DetailView):
    model = Books
    template_name = "Library/detail.html"

"""def thankyoufunction (request):
    pass
    return render (request,"Library/thankyou.html")"""


class Favorite_view(View):
    
    def post(self,request):
        id = request.POST['hidden_id']
        fav_book = Books.objects.get(pk=id)

        request.session['favorite_session']=fav_book
        
        return HttpResponseRedirect('/detail_view/' +id )

