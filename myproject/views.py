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
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            print("Yes is valid")
            form.save()
            return redirect('project')
    print('Is not post')
    return render(request, "Project_form.html", {'form': form})
