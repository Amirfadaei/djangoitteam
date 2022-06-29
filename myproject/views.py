from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
        return render(request, 'single-project.html')

def project(request, pk):
    return HttpResponse('SINGLE PROJECTS'+ ' ' + str(pk))