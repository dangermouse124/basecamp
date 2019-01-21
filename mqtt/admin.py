from django.contrib import admin
from .models import temp_10min, temp_max_min

# Register your models here.
admin.site.register(temp_max_min)
admin.site.register(temp_10min)
