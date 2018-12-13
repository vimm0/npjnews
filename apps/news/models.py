from django.db import models
from froala_editor.fields import FroalaField


class Category(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = FroalaField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Article(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
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
