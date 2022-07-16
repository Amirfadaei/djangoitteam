from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def render2(request):
    tem = 'single-project.html'
    return render(request, 'single-project.html')

def project(request, pk):
    return HttpResponse('SINGLE PROJECTS' + ' ' + str(pk))

def projects(request):
    lorem = 'projects.html'
    return render(request, 'projects.html')

def CreateProject(request):
    if request == 'post':
        form = ProjectForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('project')
    form = ProjectForm()
    return render(request, "Project_form.html", {'form': form})
