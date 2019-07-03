from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from utils.unique_slug_field_generator import unique_slug_generator
from django.db.models.signals import post_save
# Create your models here.


class Post(models.Model):

    STATUS_CHOICES = (

        ('draft', 'Draft'),

        ('published', 'Published'),

    )

    title = models.CharField(max_length=255)

    content = models.TextField()

    status = models.CharField(

        choices=STATUS_CHOICES,

        max_length=10

    )

    author = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

    )

    slug = models.SlugField(max_length=100, blank=True)

    publish = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ("-publish", )

    def __str__(self):

        return self.title


def blog_post_save_reciver(sender, instance, created, **kwargs):
    post_save.disconnect(blog_post_save_reciver, sender=Post)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

post_save.connect(blog_post_save_reciver, sender=Post)
