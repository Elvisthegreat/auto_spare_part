from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

    #Wishlist urls
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    # Testimonials
    path('products/<int:product_id>/submit_testimonial/', views.submit_testimonial, name='submit_testimonial'),
    path('products/<int:product_id>/edit_testimonial/<int:testimonial_id>/', views.testimonial_edit, name='testimonial_edit'),
    path('products/<int:product_id>/delete_testimonial/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
]