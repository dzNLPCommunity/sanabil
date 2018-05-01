from django.db import models

from base.models import Commune, Gender


class Association(models.Model):
    nom = models.CharField(max_length=500, unique=True)
    surnom = models.CharField(max_length=100, unique=True, blank=True)
    tel1 = models.CharField(max_length=20,unique=True)
    tel2 = models.CharField(max_length=20,blank=True)
    address = models.TextField()
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL,null=True)
    website = models.CharField(max_length=500, blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    youtube = models.CharField(max_length=500, blank=True)


    def __str__(self):
        return "{}.{}".format(self.id, self.nom)




class NiveauScolaire(models.Model):
    label = models.CharField(max_length=100)
    order = models.IntegerField(unique=True)


class SituationFamiliale(models.Model):
    label = models.CharField(max_length=100)


class SituationProfessionelle(models.Model):
    label = models.CharField(max_length=100)


class Individual(models.Model):
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField()
    sexe = models.ForeignKey(Gender, on_delete=models.CASCADE)
    niveau_scolaire = models.ForeignKey(NiveauScolaire, on_delete=models.CASCADE)
    tel = models.CharField(max_length=20)
    pointure = models.IntegerField() # TODO validation 20 - 50
    taille = models.CharField(max_length=100, blank=True)
    situation_familiale = models.ForeignKey(SituationFamiliale, on_delete=models.CASCADE)
    situation_professionelle = models.ForeignKey(SituationProfessionelle, on_delete=models.CASCADE)


    est_orphelin = models.BooleanField()

    association = models.ForeignKey(Association, null=True, on_delete=models.SET_NULL)



    class Meta:
        verbose_name_plural = "Nécessiteux"



class Family(models.Model):
    responsable = models.ForeignKey(Individual, on_delete=models.CASCADE)
    addresse = models.CharField(max_length=500)
    nombre_enfant =  models.SmallIntegerField(default=0)

    association = models.ForeignKey(Association, null=True, on_delete=models.SET_NULL)



class CentreType(models.Model):
    label = models.CharField(max_length=100, unique=True)

class Centre(models.Model):
    address = models.TextField()
    type = models.ForeignKey(CentreType, on_delete=models.CASCADE)
    associations = models.ManyToManyField(Association)



class Necessiteux(Individual): #, Family, Centre
    nom = models.CharField(max_length=500)

    degree_de_necissite = models.SmallIntegerField()

    class Meta:
        verbose_name_plural = "Nécessiteux"



class BesoinType(models.Model):
    label = models.CharField(max_length=100, unique=True)

class Besoin(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    type = models.ForeignKey(BesoinType, on_delete=models.CASCADE)
    necessiteux = models.ManyToManyField(Necessiteux)
    est_urgent = models.BooleanField(default=False)
    date_limite = models.DateField()
    montant = models.IntegerField(default=0)
    planification_date = models.DateField()
    giving_date = models.DateField(blank=True, null=True)
    is_don_given = models.BooleanField(default=False)


class DonType(models.Model):
    label = models.CharField(max_length=100, unique=True)

class DonneurType(models.Model):
    label = models.CharField(max_length=100, unique=True)


class Donneur(models.Model):
    nom =  models.CharField(max_length=100)
    type = models.ForeignKey(DonneurType, on_delete=models.CASCADE)
    est_active = models.BooleanField(default = False)
    should_be_anonyme =  models.BooleanField(default = True)
    tel = models.CharField(max_length=20)


class Don(models.Model):
    type  = models.ForeignKey(DonType, on_delete=models.CASCADE)
    valuer = models.TextField()
    recieving_date = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return
