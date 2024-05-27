from django.urls import path

# Import views
from . import views

app_name = 'users'

urlpatterns = [

    path('register/',views.register_view,name="register"), 

    path('login/',views.login_view,name="login"),

]