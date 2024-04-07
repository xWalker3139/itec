from django.contrib import admin
from .models import Aplicatie, Endpoint, Bug, SetariUtilizator

admin.site.register(Aplicatie)
admin.site.register(Endpoint)
admin.site.register(Bug)
admin.site.register(SetariUtilizator)

# Register your models here.
