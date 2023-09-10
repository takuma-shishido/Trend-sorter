from django.db import models

class Repository(models.Model):
    span = models.TextField()
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()
    lang = models.CharField(max_length=255)
    star = models.IntegerField(default=0)
    star_by_span = models.IntegerField(default=0)
    fork = models.IntegerField(default=0)

    def value(self):
        return self
