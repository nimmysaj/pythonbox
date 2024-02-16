from django.contrib import admin
from django.contrib.admin import ModelAdmin

from shop.models import category, product


# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(category,categoryadmin)
admin.site.register(product,productadmin)