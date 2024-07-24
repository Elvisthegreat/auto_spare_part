from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name