from django.contrib import admin
from .models import ContactMessage, SlideModel

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(SlideModel)