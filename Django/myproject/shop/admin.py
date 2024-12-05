from django.contrib import admin
from .models import Category,Product

class AdminCategorie(admin.ModelAdmin):
    list_display=('nom', 'date_add' )

class AdminPruduct(admin.ModelAdmin):
    list_display=('titre', 'prix', 'category','date_add')

admin.site.register(Product, AdminPruduct)
admin.site.register(Category,AdminCategorie)

# Register your models here.
