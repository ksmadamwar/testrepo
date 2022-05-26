from django.contrib import admin

# Register your models here.

from .models import UserInformation,CholinesteraseType,BiosensorTestType,SensorData

admin.site.register(UserInformation)
admin.site.register(CholinesteraseType)
admin.site.register(BiosensorTestType)
admin.site.register(SensorData)
