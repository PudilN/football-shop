import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
    ('sepak_bola', 'Sepak Bola'),
    ('jersey', 'Jersey'),
    ('sepatu', 'Sepatu'),
    ('pelindung', 'Pelindung'),
    ('lainnya', 'Lainnya'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='sepak_bola')
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    release_date = models.DateField(null=True, blank=True)
    reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.brand}"
    
    dawd