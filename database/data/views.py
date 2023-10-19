from django.shortcuts import render,get_object_or_404
from .models import fun

def index(request):
    mvlist = fun.objects.all()
    return render(request,"data/index.html",{"movies":mvlist})

# Create your views here.
# Create your views here.
def MovieDetails(request,slug):
    #moviedetial=fun.objects.get(pk=id)
    moviedetial = get_object_or_404(fun,slug = slug)

    return render(request,"data/moviedetails.html",

                  {
                      "title": moviedetial.title,
                      "director":moviedetial.director,
                      "verdict":moviedetial.verdict,
                      "rating":moviedetial.rating

                  }

                  )