from django.urls import path
from . import views


urlpatterns = [

    path('projects/', views.projects, name="navbar"),
    path('single/', views.render2, name="render"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create-project/', views.CreateProject, name="Add_Project"),

]