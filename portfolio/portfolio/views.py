from __future__ import unicode_literals
from django.shortcuts import render
from projects.models import Project


def index_page(request):
    projects = Project.objects.all()
    return render(request, 'index.html', context={'projects': projects})
