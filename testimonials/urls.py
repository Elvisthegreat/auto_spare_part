from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/submit_testimonial/', views.submit_testimonial, name='submit_testimonial'),
    path('edit_testimonial/<int:testimonial_id>/', views.testimonial_edit, name='testimonial_edit'),
    path('delete_testimonial/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
]
