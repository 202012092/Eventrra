from django.db import models

# Create your models here.
class EventHostAccounts(models.Model):
    eventhost_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class VenueHolderAccounts(models.Model):
    venueholder_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class EventCategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100,unique=True)

class Venues(models.Model):
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=100)
    venue_address = models.TextField()
    venue_description = models.TextField()
    venue_cost = models.IntegerField()
    venue_capacity = models.IntegerField()
    venue_seating_type = models.CharField(max_length=50)
    venue_special_features = models.CharField(max_length=100)
    category_id = models.ForeignKey('EventCategories',on_delete=models.CASCADE)
    venue_holder_id = models.ForeignKey('VenueHolderAccounts',on_delete=models.CASCADE)