from django.contrib import admin
from .models import ContactMessage, SlideModel, Review, Gallery

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(SlideModel)
admin.site.register(Review)
admin.site.register(Gallery)
