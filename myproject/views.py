from django.shortcuts import render
from django.http import HttpResponse


def render(request):
    return render(request, 'single-project.html')


def projects(request):
    return render(request, 'projects.html')


def project(request, pk):
    return HttpResponse('SINGLE PROJECTS' + ' ' + str(pk))
