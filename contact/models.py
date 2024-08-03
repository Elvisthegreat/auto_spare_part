from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactRequest(models.Model):
    """Models for recording user contact request"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255,)
    email = models.EmailField(max_length=255, unique=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        """Check if the email already exists in the database."""
        if ContactRequest.objects.filter(email=self.email).exists():
            raise ValidationError(f"Email {self.email} already exists.")
        super(ContactRequest, self).save(*args, **kwargs)