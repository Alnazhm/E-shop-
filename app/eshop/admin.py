from django.contrib import admin
from eshop.models import Product
from eshop.models import Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'image')
    list_filter = ('id', 'name', 'category', 'description', 'image', 'created_at', 'updated_at')
    search_fields = ('name', 'category', 'description')
    fields = ('name', 'category', 'description', 'image')


admin.site.register(Product, ProductAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'description', 'score')
    list_filter = ('id', 'author', 'product', 'description', 'score', 'created_at', 'updated_at')
    search_fields = ('author', 'product', 'description', 'score')
    fields = ('author', 'product', 'description', 'score')

admin.site.register(Review, ReviewAdmin)
