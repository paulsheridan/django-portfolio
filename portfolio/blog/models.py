from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class BlogEntry(models.Model):
    """
    Blog entry model for individual
    posts. Includes optional comic image
    field.
    """
    title = models.CharField(max_length=255)
    body_text = models.CharField(max_length=255)
    comic = models.ImageField(upload_to='media/%Y-%m-%d', default='')
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
