from django.db import models


class Tag(models.Model):
    created = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text


class DummyTable(models.Model):
    created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
