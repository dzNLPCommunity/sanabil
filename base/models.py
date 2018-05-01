from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


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
    post_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {} - {} ".format(self.id, self.name, self.wilaya.name)


class Gender(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    name = models.CharField(max_length=20)
    icon = models.ImageField(blank="", null="")

    def __str__(self):
        return "{} ({})".format(self.name, self.id)

class Parameter(models.Model):
    name = models.CharField(max_length=40, unique=True)
    value = models.CharField(max_length=100)
    type = models.CharField(max_length=10,choices=[('int','Integer'),('bool','Boolean')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{} ({})".format(self.name, self.type)


class PhoneType(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class AgeCategory(models.Model):
    name = models.CharField(max_length=50)
    lower_limit = models.PositiveSmallIntegerField(validators=[MaxValueValidator(120), MinValueValidator(13)])
    upper_limit = models.PositiveSmallIntegerField(validators=[MaxValueValidator(120), MinValueValidator(13)])

    def __str__(self):
        return "{} ({} - {})".format(self.name, self.lower_limit, self.upper_limit)

    class Meta:
        verbose_name_plural = "Age categories"
