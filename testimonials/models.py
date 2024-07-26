from django.contrib.auth.models import User
from django.db import models
from products.models import Product

# Create your models here.

class Testimonial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='testimonial')
    name = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='testimonials')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.product.name}"
