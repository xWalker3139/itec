from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Aplicatie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nume = models.CharField(max_length = 256, null=True, blank=False)
    descriere = models.CharField(max_length = 624, null=True, blank=False)

    def __str__(self):
        return self.nume

class Endpoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    aplicatie = models.ForeignKey(Aplicatie, on_delete=models.CASCADE, null=True)
    nume = models.CharField(max_length=255, null=True)
    url = models.URLField(max_length=1024, null=True)
    metoda_http = models.CharField(max_length=10, choices=(('GET', 'GET'), ('POST', 'POST')), default='GET', null=True)
    stare = models.CharField(max_length = 256, null=True, default="Unknown")

    def __str__(self):
        return self.nume


class Bug(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    aplicatie = models.ForeignKey(Aplicatie, on_delete=models.CASCADE)
    descriere = models.CharField(max_length=624, null=True, blank=False)

    def __str__(self):
        return str(self.descriere)

class SetariUtilizator(models.Model):
    utilizator = models.OneToOneField(User, on_delete=models.CASCADE, related_name='setari')
    interval_verificare = models.CharField(max_length=264, default=60)

    def __str__(self):
        return self.interval_verificare


# Create your models here.
