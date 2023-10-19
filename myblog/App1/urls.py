from . import views
from django.urls import path


urlpatterns = [
    path("", views.index,name="Home"),
    path("posts",views.posts,name="posts"),
    path("posts/<slug:slug>",views.posts_slug,name="slug")
]
