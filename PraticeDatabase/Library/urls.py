from . import views

from django.urls import path

urlpatterns = [
    
    path("",views.create_view.as_view()),
    path('thankyou', views.Thank_you.as_view()),
    path("reviews_list",views.Reviews_List.as_view()),
    path("detail_view/favorite",views.Favorite_view.as_view()),
    path("reviews_list/<int:id>",views.single_review_page.as_view()),
    path("detail_view/<int:pk>",views.view_detail.as_view())

]

#path("",views.view_class.as_view()),     this has been removed because we are using the from formview
#rather than View

# path("",views.form_view.as_view()),  rather than using forms view we use create view to lesser code\
#hence no need to over ride any method 

#path('', views.forms_home,name="index") funtion view not  class view 