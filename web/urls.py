from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "web"
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('shoemart',views.shoemart,name="shoemart"),
    path('signup',views.signup ,name="signup"),
    path('login',views.login_1 ,name="login"),

]
