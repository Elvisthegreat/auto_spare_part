from django.urls import path
from . import views

urlpatterns = [
    path('submit_testimonial/<int:product_id>/', views.submit_testimonial, name='submit_testimonial'),
    path('testimonials/', views.testimonials, name='testimonials'),
]
