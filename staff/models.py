from django.contrib.auth.models import  AbstractUser
from django.db import models

from staff.constants import PROFILE_TYPES


class Membre(AbstractUser):
    profile = models.IntegerField(choices=PROFILE_TYPES, default=1)

    def __str__(self):
        return "{}".format(self.username)

    class Meta:
        verbose_name_plural = "Membres"
        verbose_name = "Membre"

class Login(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()


    def __str__(self):
        return "{} {} {}".format(self.membre, self.ip, self.created_at)



