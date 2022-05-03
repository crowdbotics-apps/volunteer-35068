from django.conf import settings
from django.db import models


class Customuser(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    lastname = models.CharField(
        max_length=256,
    )
    patronomic = models.CharField(
        max_length=256,
    )
    date_brithday = models.DateField()
