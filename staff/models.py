from django.contrib.auth.models import AbstractUser
from django.db import models

from staff.constants import PROFILE_TYPES, ROLE_CHOICES


class Role(models.Model):
    primary = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    secondary = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('primary', 'secondary')

    def __str__(self):
        return "{} - {}".format(self.get_primary_display(), self.secondary)



class User(AbstractUser):
    roles = models.ManyToManyField(Role)



class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True)
    type = models.IntegerField(choices=PROFILE_TYPES)


    def __str__(self):
        return "{}".format(self.user)



class Login(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    agent = models.ForeignKey(Membre, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()


    def __str__(self):
        return "{} {} {}".format(self.employee, self.ip, self.created_at)



