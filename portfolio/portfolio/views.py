from __future__ import unicode_literals
from django.shortcuts import render, redirect
from projects.models import Project
from projects.forms import ProjectForm


def index_page(request):
    projects = Project.objects.all()
    return render(request, 'index.html', context={'projects': projects})


def add_project(request):
    form = ProjectForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index_page')
    return render(request, 'newedit.html', context={'form': form})
