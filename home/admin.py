from cmath import pi
from django.contrib import admin

# Register your models here.
from .models import pictureModel,profile

admin.site.register(pictureModel)
admin.site.register(profile)