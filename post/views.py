from django.shortcuts import render
from django.views import generic
from .models import Post, Tag
# Create your views here.

class BlogHome(generic.ListView):

    model = Post

    paginate_by = 4

    template_name = 'post/home.html'

    def get_context_data(self):

        ctx = super().get_context_data()

        ctx['tags'] = Tag.objects.all()

        return ctx