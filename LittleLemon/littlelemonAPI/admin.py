from django.contrib import admin

# Register your models here.
from .models import Booking, MenuItem

admin.site.register(Booking)
admin.site.register(MenuItem)