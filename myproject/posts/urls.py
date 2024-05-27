from django.urls import path

# Import views
from . import views

app_name = 'posts'

urlpatterns = [

    path('',views.posts_list,name="list"),   #add a path to the home page
    path('<slug:slug>',views.post_page,name="page"),


]