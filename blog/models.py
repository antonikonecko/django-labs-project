from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 50, default = "")

    class Meta:
        verbose_name_plural = 'authors'


    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_publish = models.DateTimeField(blank=True, null=True)
    public = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    # author = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.title


