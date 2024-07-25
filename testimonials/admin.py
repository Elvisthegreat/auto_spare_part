from django.contrib import admin
from .models import Testimonial

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'message',
        'create_at',
    )

admin.site.register(Testimonial)

