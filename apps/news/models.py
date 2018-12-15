from django.db import models
from froala_editor.fields import FroalaField


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300)
    description = FroalaField()
    cat_od = models.PositiveIntegerField(default=0, editable=True, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('cat_od',)


class Reporter(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = FroalaField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    publications = models.ManyToManyField(Publication)
    category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
