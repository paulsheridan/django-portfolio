from django.db import models
# from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Project(models.Model):
    """
    CS Project model for individual
    projects. Includes all necessary info
    for a portfolio entry.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='projects')
    published = models.DateField()
    github = models.URLField(max_length=50)
    url = models.URLField(max_length=50, blank=True)
    button_text = models.CharField(max_length=20, default='Visit Page')
