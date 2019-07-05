from django import template
from post.models import Post
from django.db.models import Count

register = template.Library()

@register.simple_tag
def get_total_post_count():
    return Post.objects.count()

@register.inclusion_tag('post/latest_post.html')
def get_latest_posts(count=5):

    posts = Post.objects.all()[:count]

    return {"latest_posts": posts}

@register.simple_tag
def get_most_commented_post(count=5):

    return Post.objects.annotate(
        comment_count=Count('comment')
    ).order_by('comment_count')