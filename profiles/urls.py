from django.urls import path

from . import views

urlpatterns = [
   path("", views.CreateProfileView.as_view()),
   path("list_view",views.List_view_table.as_view())
   
]




 #path("", views.Create_view_for_upload.as_view()),
 #path("", views.CreateProfileView.as_view()),