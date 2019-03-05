from django.db import models
from django.views.generic import TemplateView


class Image(models.Model):
    title = models.CharField(max_length=300)
    image = models.URLField()
    description = models.TextField()

