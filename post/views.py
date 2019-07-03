from django.shortcuts import render
from django.views import generic

# Create your views here.

class BlogHome(generic.TemplateView):

    template_name = 'post/home.html'
