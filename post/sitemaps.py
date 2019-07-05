from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSiteMap(Sitemap):

    changeferq = 'weekly'

    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmode(self, obj):

        return obj.updated


class PostSitemap(Sitemap):
    
    changefreq = 'weekly'


    priority = 0.9


    def items(self):


        return Post.objects.all()


    def lastmod(self, obj):


        return obj.updated_at
