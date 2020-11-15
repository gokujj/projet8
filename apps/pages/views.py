from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"


class LegalView(TemplateView):
    template_name = "pages/legal.html"