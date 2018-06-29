from django.db import models

from base.models import Commune, NiveauScolaire, SituationFamiliale, SituationProfessionelle, CentreType, \
    DonType, DonneurType
from staff.models import Membre

class Association(models.Model):
    responsable = models.ForeignKey(Membre, on_delete=models.SET_NULL, null=True, limit_choices_to={ "profile": 2 })
    nom = models.CharField(max_length=500, unique=True)
    surnom = models.CharField(max_length=100, unique=True, blank=True)
    telephone = models.CharField(max_length=20,unique=True)
    telephone_2 = models.CharField(max_length=20,blank=True)
    address = models.TextField()
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL,null=True)
    website = models.CharField(max_length=500, blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    youtube = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return "{}.{}".format(self.id, self.nom)


class Famille(models.Model):
    nom = models.CharField(max_length=500)
    nombre_enfant =  models.SmallIntegerField(default=0)

    def __str__(self):
        return "{}".format(self.nom)

class Necessiteux(models.Model):
    nom = models.CharField(max_length=500)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices = [("F", "Female"), ("M", "Male")])
    niveau_scolaire = models.ForeignKey(NiveauScolaire, on_delete=models.CASCADE)
    tel = models.CharField(max_length=20)
    pointure = models.IntegerField() # TODO validation 20 - 50
    taille = models.CharField(max_length=100)
    situation_familiale = models.ForeignKey(SituationFamiliale, on_delete=models.CASCADE)
    situation_professionelle = models.ForeignKey(SituationProfessionelle, on_delete=models.CASCADE)


    est_orphelin = models.BooleanField()

    appartient_famille = models.ForeignKey(Famille, on_delete=models.CASCADE)
    represent_famille = models.BooleanField(default=False)
    association = models.ForeignKey(Association, null=True, on_delete=models.SET_NULL, related_name="members")
    degre_necessite = models.SmallIntegerField(default=0)


    archive = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Necessiteux"


    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)


class Centre(models.Model):
    nom = models.CharField(max_length=500)
    address = models.TextField()
    type = models.ForeignKey(CentreType, on_delete=models.CASCADE)
    associations = models.ManyToManyField(Association)

    def __str__(self):
        return "{} ({})".format(self.nom, self.type)

class Besoin(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    type = models.ForeignKey(DonType, on_delete=models.CASCADE)
    necessiteux = models.ManyToManyField(Necessiteux)
    est_urgent = models.BooleanField(default=False)
    date_limite = models.DateField()
    montant = models.IntegerField(default=0)
    date_planification = models.DateField()
    date_remise_don = models.DateField(blank=True, null=True)
    besoin_satisfait = models.BooleanField(default=False)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)

class Donneur(models.Model):
    nom =  models.CharField(max_length=100)
    type = models.ForeignKey(DonneurType, on_delete=models.CASCADE)
    est_active = models.BooleanField(default = False)
    anonyme =  models.BooleanField(default = True)
    tel = models.CharField(max_length=20, blank=True)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)


    def __str__(self):
        return "{} ({})".format(self.nom, self.type)


class AideRecu(models.Model):
    type = models.ForeignKey(DonType, on_delete=models.CASCADE)
    description = models.TextField()
    date_reception = models.DateField()
    donneur =  models.ForeignKey(Donneur, on_delete=models.CASCADE)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)

    def __str__(self):
        return "Don #{} ({})".format(self.id, self.type)



