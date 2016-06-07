from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Project(models.Model):
    """
    CS Project model for individual
    projects. Includes all necessary info
    for a portfolio entry.
    """
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/projects')
    published = models.CharField(max_length=30)
    github = models.URLField(max_length=50)
    url = models.URLField(max_length=50)
    button_text = models.CharField(max_length=20, default='Visit Page')
