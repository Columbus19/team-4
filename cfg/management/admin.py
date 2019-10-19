from django.contrib import admin
from .models import User, Corporation, Application

admin.site.register(User)
admin.site.register(Corporation)
admin.site.register(Application)
# Register your models here.
