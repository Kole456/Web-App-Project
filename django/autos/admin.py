from django.contrib import admin

# assignment stuffs
from .models import Auto, Make

admin.site.register(Make)
admin.site.register(Auto)
