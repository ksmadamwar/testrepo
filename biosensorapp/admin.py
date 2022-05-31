from django.contrib import admin

# Register your models here.

from .models import UserInformation,SensorData

admin.site.register(UserInformation)
admin.site.register(SensorData)
