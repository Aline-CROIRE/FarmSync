from django.contrib import admin

from region_app import models

admin.site.register(models.User)
admin.site.register(models.Cooperative)
admin.site.register(models.Fail_type)
admin.site.register(models.Quality)
admin.site.register(models.Stock_management)
admin.site.register(models.System)
admin.site.register(models.Message)
admin.site.register(models.Notification)
admin.site.register(models.Geolocation)
