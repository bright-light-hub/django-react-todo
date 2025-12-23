from django.contrib import admin
from .models import TODO
# Register your models here.

# BL- ragister the todo model in the admin panel
admin.site.register(TODO)