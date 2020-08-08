from django.contrib import admin
from .models import Image, Profile, Comments
admin.site.site_header='Developer'

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comments)
