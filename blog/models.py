from django.db import models
from django.contrib.auth.models import User
from .functions import weekdict

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    color = models.TextField()
    hovercolor = models.TextField()
    day = models.TextField()
    week = models.TextField()
    month = models.TextField()
    dayyear = models.TextField()
    streak = models.IntegerField(null=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    habit = models.CharField(max_length=150)

    def __str__(self):
        return str(self.user)

class Record(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    weekcolor = models.JSONField({"Monday": "#808080", "Tuesday": "#808080", "Wednesday": "#808080",
                                  "Thursday": "#808080", "Friday": "#808080", "Saturday": "#808080", "Sunday": "#808080"}, null=True)

    def __str__(self):
        return str(self.user)