from django.contrib import admin

# Register your models here.

from . models import Category , Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',)}
    
@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('title',)} 
    """ automatically being prepopulated with the title (urlstyle) of the product
    Nike air jordan -> nike-air-jordan """
    
    
