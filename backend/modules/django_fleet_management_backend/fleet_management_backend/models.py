from django.db import models


class Equipment(models.Model):
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    image = models.URLField()
    basicStats = models.JSONField()

    def __str__(self):
        return f'{self.type} - {self.status}'


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=100)
    permissions = models.JSONField()

    def __str__(self):
        return self.username
