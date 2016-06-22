from django import forms
from django.db import models
from projects.models import Project


class ProjectForm(forms.ModelForm):
    description = models.CharField(max_length=1000,
                                   attrs={'class': 'u-full-width'}
                                   )
    url = models.URLField(required=False)

    class Meta:
        model = Project
        fields = ['title',
                  'image',
                  'published',
                  'github',
                  'button_text']
