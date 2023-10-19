from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse



def index(request):

    return render(request, "App1/index.html")
    pass

def posts(request):

    return render(request,"App1/All_myposts.html")
    pass

def posts_slug(request):
    pass