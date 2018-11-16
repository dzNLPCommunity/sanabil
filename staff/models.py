import six
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.db import models

from base.models import Commune
from staff.constants import PROFILE_TYPES


class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    prénom = models.CharField(max_length=30)
    nom = models.CharField( max_length=50)
    email = models.EmailField()
    tel = models.CharField(max_length=50)
    profil = models.IntegerField(choices=PROFILE_TYPES, default=1)
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()

    username = models.CharField(
        'username',
        null=False,
        blank=False,
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    password = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return "{}".format(self.username)

    class Meta:
        verbose_name_plural = "Membres"
        verbose_name = "Membre"

    def save(self, *args, **kwargs):
        if not self.id:
            username = self.username or "%s_%s" % (
            self.nom.lower().strip().replace(' ', '_'), self.prénom.lower().strip().replace(' ', '_'))
            password = self.password or User.objects.make_random_password(length=8,
                                                                          allowed_chars='abcdefghjkmnpqrstuvwxyz')
            new_user = User.objects.create_user(username=username,
                                                email=self.email,
                                                password=password)
            self.password = password
            self.user = new_user

        super(Membre, self).save()  # force_update=force_update


class Association(models.Model):
    responsable = models.ForeignKey(Membre, on_delete=models.SET_NULL, blank=True, null=True,
                                    limit_choices_to={"profil": 2})
    nom = models.CharField(max_length=500, unique=True)
    surnom = models.CharField(max_length=100, unique=True, blank=True)
    telephone = models.CharField(max_length=20, unique=True)
    telephone_2 = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL,null=True)
    website = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    youtube = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "{}.{}".format(self.id, self.nom)


class Login(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()


    def __str__(self):
        return "{} {} {}".format(self.membre, self.ip, self.created_at)


