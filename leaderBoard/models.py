from django.db import models

class Leaderboard(models.Model):
    UID = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    score = models.IntegerField()
    country = models.CharField(max_length=2)
    timestamp = models.DateTimeField(auto_now_add=True)

