from django.db import models

from base.models import Commune, NiveauScolaire, SituationFamiliale, SituationProfessionelle, CentreType, \
    DonType, DonneurType
from staff.models import Membre

class Association(models.Model):
    responsable = models.ForeignKey(Membre, on_delete=models.SET_NULL, blank=True, null=True, limit_choices_to={ "profile": 2 })
    nom = models.CharField(max_length=500, unique=True)
    surnom = models.CharField(max_length=100, unique=True, blank=True)
    telephone = models.CharField(max_length=20,unique=True)
    telephone_2 = models.CharField(max_length=20,null=True, blank=True)
    address = models.TextField()
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL,null=True)
    website = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    youtube = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "{}.{}".format(self.id, self.nom)


class Famille(models.Model):
    nom = models.CharField(max_length=500)
    nombre_enfant =  models.SmallIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nom)

class Necessiteux(models.Model):
    association = models.ForeignKey(Association, null=True, on_delete=models.SET_NULL, related_name="members")
    nom = models.CharField(max_length=500)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField(blank=True, null=True)
    sexe = models.CharField(max_length=1, choices = [("F", "Female"), ("M", "Male")])
    niveau_scolaire = models.ForeignKey(NiveauScolaire, on_delete=models.SET_NULL, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    pointure = models.IntegerField(blank=True, null=True) # TODO validation 20 - 50
    taille = models.CharField(max_length=100, blank=True, null=True)
    situation_familiale = models.ForeignKey(SituationFamiliale, on_delete=models.SET_NULL, blank=True, null=True)
    situation_professionelle = models.ForeignKey(SituationProfessionelle, on_delete=models.SET_NULL, blank=True, null=True)
    est_orphelin = models.BooleanField()
    degré_nécessite = models.SmallIntegerField(default=0, choices = [(0, '0'), (1, '1'), (2, '2'), (3, '3') , (4, '4'), (5, '5')])
    appartient_famille = models.ForeignKey(Famille, on_delete=models.SET_NULL, blank=True, null=True)
    represent_famille = models.BooleanField(default=False)
    archivé = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Nécessiteux"
        verbose_name = "Nécessiteux"


    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)


class Centre(models.Model):
    nom = models.CharField(max_length=500)
    address = models.TextField()
    type = models.ForeignKey(CentreType, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.nom, self.type)

class Besoin(models.Model):
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    necessiteux = models.ForeignKey(Necessiteux, on_delete=models.CASCADE, null=True, blank=True)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(DonType, on_delete=models.CASCADE)
    est_urgent = models.BooleanField(default=False)
    date_limite = models.DateField(blank=True, null=True)
    montant = models.IntegerField(default=0, null=True, blank=True)
    date_planification = models.DateField(blank=True, null=True)
    date_remise_don = models.DateField(blank=True, null=True)
    est_satisfait = models.BooleanField(default=False)


    def __str__(self):
        return "{}. {}".format(self.id, self.nom)

class Donneur(models.Model):
    nom =  models.CharField(max_length=100)
    tel = models.CharField(max_length=20, null=True, blank=True)
    type = models.ForeignKey(DonneurType, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default = False)
    anonyme =  models.BooleanField(default = True)


    def __str__(self):
        return "{} ({})".format(self.nom, self.type)


class AideRecu(models.Model):
    donneur =  models.ForeignKey(Donneur, on_delete=models.SET_NULL, null=True)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    type = models.ForeignKey(DonType, on_delete=models.SET_NULL, null=True)
    date_reception = models.DateField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Aide reçu"
        verbose_name_plural = "Aides reçus"

    def __str__(self):
        return "Don #{} ({})".format(self.id, self.type)



