from django.urls import path

# Import views
from . import views


urlpatterns = [

    path('',views.posts_list),   #add a path to the home page

]