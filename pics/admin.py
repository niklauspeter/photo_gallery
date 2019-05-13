from django.contrib import admin

# Register your models here.
from .models import Category,Areas,Image,tags

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Category)
admin.site.register(Areas)
admin.site.register(Image,ImageAdmin )
admin.site.register(tags)
