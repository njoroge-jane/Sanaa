from django.contrib import admin

# Register your models here.
from .models import Location,Category,Image

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)