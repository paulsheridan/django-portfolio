from __future__ import unicode_literals
from django.views.generic import ListView
from projects.models import Project
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProjectList(ListView):
    template_name = 'index.html'
    context_object_name = 'projects'
    queryset = Project.objects.order_by('-published')


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class ProjectDelete(DeleteView):
    template_name = 'delete.html'
    model = Project
    success_url = '/'


def view_resume(request):
    with open('media/PaulSheridanCV.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=paulsheridancv.pdf'
        return response
    pdf.closed
