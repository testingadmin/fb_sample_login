from django.db import models


class UserPerson(models.Model):
    name = models.CharField(max_length=70, null=True, blank=True)
    password = models.CharField(max_length=70, null=True, blank=True)

