from msilib.schema import PublishComponent
from statistics import mode
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    class NewManager(models.Manager):

        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=128)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=128, unique_for_date="publish")
    publish = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()
    newmanager = NewManager()

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_single", kwargs={"post": self.slug})
