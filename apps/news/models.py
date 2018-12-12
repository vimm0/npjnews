from django.db import models
from froala_editor.fields import FroalaField


class News(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = FroalaField()
