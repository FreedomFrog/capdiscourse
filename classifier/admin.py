from django.contrib import admin
from classifier import models


# Register your models here.
admin.site.register(models.UserText)
admin.site.register(models.Topic)