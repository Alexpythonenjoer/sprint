from django.db import models
from rest_framework import serializers

class TouristData(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    coordinates = models.CharField(max_length=255)
    height = models.FloatField()
    name = models.CharField(max_length=255)
    images = models.JSONField()
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

class TouristDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristData
        fields = ['coordinates', 'height', 'name', 'images', 'username', 'email', 'phone', 'status']
# Create your models here.
