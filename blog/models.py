from msilib.schema import PublishComponent
from statistics import mode
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique_for_date="publish")
    publish = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
