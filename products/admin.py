from django.contrib import admin
from .models import Product, Category, Wishlist, Testimonial

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # tuple that will tell the admin which fields to display.
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    # sort the products by SKU using the ordering attribute.
    # for reverse we can just add - minus
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'product'
        'name',
        'message',
        'create_at',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist)
admin.site.register(Testimonial)
