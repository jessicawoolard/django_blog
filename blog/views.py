from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Image


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        images = Image.objects.all()

        context = {
            'images': images
        }

        return context
