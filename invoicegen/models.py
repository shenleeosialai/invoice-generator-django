from django.db import models

class Invoice(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_number = models.CharField(max_length=100, unique=True)
    client_name = models.CharField(max_length=200, blank=True)
    client_address = models.TextField(blank=True)
    client_city = models.CharField(max_length=100, blank=True)
    client_country = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['invoice_number']),
        ]    