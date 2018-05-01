from django.db import models
from fcm_django.models import FCMDevice

from staff.models import User


class Notification(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    icon = models.ImageField(blank=True, null=True)
    texte = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    importance = models.IntegerField(default=5)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    sent = models.BooleanField(default=False)
    recieved = models.BooleanField(default=False)
    vue = models.BooleanField(default=False)

    def __str__(self):
        return "%s. %s" % (self.id, self.texte)

    def save(self, *args, **kwargs):
        try:
            if self.utilisateur:
                device = FCMDevice.objects.get(user_id=self.utilisateur.id, active=True)
                print(device.registration_id)
                device.send_message(title=self.titre, body=self.texte, sound=True, data={"type": self.type})
            else:
                devices = FCMDevice.objects.all()
                devices.send_message(title=self.titre, body=self.texte, sound=True, data={"type": self.type})
        except:
            pass

        super(Notification, self).save()
