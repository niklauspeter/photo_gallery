from django.contrib import admin

# Register your models here.
from .models import Category,Areas,Image,tags

admin.site.register(Category)
admin.site.register(Areas)
admin.site.register(Image)
admin.site.register(tags)
