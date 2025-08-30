from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    class Meta:
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=50)
    members = models.JSONField()
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        db_table = 'activities'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    user_email = models.EmailField()
    workout = models.CharField(max_length=100)
    class Meta:
        db_table = 'workouts'
