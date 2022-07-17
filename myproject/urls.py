from django.urls import path
from . import views


urlpatterns = [

    path('projects/', views.projects, name="navbar"),
    path('single/', views.render2, name="render"),
    path('project/', views.render2, name="project"),
    path('create-project/', views.CreateProject, name="Add_Project"),

]