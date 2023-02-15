from django.urls import path
from recipes import views

appname="recipes"

urlpatterns = [
    path('', views.home),
    path('sobre/', views.sobre),
    path('contato/', views.contato),

]