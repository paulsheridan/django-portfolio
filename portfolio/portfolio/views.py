from __future__ import unicode_literals
from django.views.generic import ListView
from projects.models import Project
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


class ProjectList(ListView):
    template_name = 'index.html'
    context_object_name = 'projects'
    queryset = Project.objects.order_by('-published')


class ProjectCreate(CreateView):
    template_name = 'newedit.html'
    model = Project
    fields = ['title',
              'description',
              'image',
              'published',
              'github',
              'url',
              'button_text']
    success_url = '/'


class ProjectUpdate(UpdateView):
    template_name = 'newedit.html'
    model = Project
    fields = ['title',
              'description',
              'image',
              'published',
              'github',
              'url',
              'button_text']
    success_url = '/'


class ProjectDelete(DeleteView):
    template_name = 'delete.html'
    model = Project
    success_url = '/'
