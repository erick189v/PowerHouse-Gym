from django.contrib import admin

# Register your models here.
from .models import Journey, RepSet

admin.site.register(Journey)
admin.site.register(RepSet)