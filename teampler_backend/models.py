from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)

    grade = models.IntegerField()
    major = models.CharField(max_length=100)

class Group(models.Model):
    title = models.CharField(max_length=250)
    
    admin = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="user_as_admin")
    members = models.ManyToManyField(UserData, related_name="user_as_member")