from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    message = models.TextField(blank=True)
    documents = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    contact_date = models.DateTimeField(default=datetime.now)
    user_id = models.IntegerField(blank=True)
    def __str__ (self):
        return self.name