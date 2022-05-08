from django.shortcuts import render
from tempfile import template
# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'