from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):

    STATUS_CHOICES = (

        ('draft', 'Draft'),

        ('published', 'Published'),

    )

    title = models.CharField(max_length=255)

    content = RichTextUploadingField()

    status = models.CharField(

        choices=STATUS_CHOICES,

        max_length=10

    )

    author = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

    )

    slug = models.SlugField(max_length=100)

    publish = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ("-publish", )

    def __str__(self):

        return self.title
