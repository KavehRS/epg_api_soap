from django.db import models


class Note(models.Model):
    channel = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    duration = models.IntegerField()
    visit = models.IntegerField(max_length=200)
    month = models.CharField(max_length=200)
