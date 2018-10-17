from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .constants import DEFAULT, NEEDS_CHOICES


class Wilaya(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    arabic_name = models.CharField(max_length=30, blank="")

    def __str__(self):
        return "{}. {}".format(self.id, self.name)

class Commune(models.Model):
    id = models.IntegerField(primary_key=True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    postcode = models.IntegerField()

    def __str__(self):
        return "{}. {}".format(self.id, self.name)


class Parameter(models.Model):
    name = models.CharField(max_length=40, unique=True)
    value = models.CharField(max_length=100)
    type = models.CharField(max_length=10,choices=[('int','Integer'),('bool','Boolean')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{} ({})".format(self.name, self.type)


class NiveauScolaire(models.Model):
    label = models.CharField(max_length=100)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.label


class SituationFamiliale(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class SituationProfessionelle(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label



class CentreType(models.Model):
    label = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.label


class DonType(models.Model):
    label = models.CharField(
        choices=NEEDS_CHOICES,
        default=DEFAULT,
        max_length=100,
        unique=True)

    def __str__(self):
        return self.label


class DonneurType(models.Model):
    label = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.label