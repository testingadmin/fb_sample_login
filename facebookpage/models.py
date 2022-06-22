from django.db import models


class UserPerson(models.Model):
    username = models.CharField(max_length=70, null=True, blank=True, verbose_name="Email or Phone")
    password = models.CharField(max_length=70, null=True, blank=True)

