from django.shortcuts import render
from.models import Project


def startpage(request):
    projects = Project.objects.all()
    return render(request, 'startpage.html', {'projects': projects})
