from django.contrib import admin
from products.models import Product, ProductCategory, Basket


# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name', 'price')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    extra = 0
    readonly_fields = ('created_timestamp',)

