from django.http import HttpResponse
from django.shortcuts import render


def render2(request):
    tem = 'single-project.html'
    return render(request, 'single-project.html')

def project(request, pk):
    return HttpResponse('SINGLE PROJECTS' + ' ' + str(pk))

def projects(request):
    lorem = 'project.html'
    return render(request, 'projects.html')
