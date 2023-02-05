from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username


class Question(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255, blank=True)
    link = models.URLField(unique=True)
    notes = models.TextField(blank=True)
    video_solution = models.URLField(unique=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    time_complexity = models.CharField(max_length=255, null=True, blank=True)
    space_complexity = models.CharField(max_length=255, null=True, blank=True)
    time_to_solve = models.IntegerField(null=True, blank=True)
    optimized = models.BooleanField(default=False)  
    date = models.DateTimeField(blank=True, null=True) 

    def __str__(self):
        return self.name