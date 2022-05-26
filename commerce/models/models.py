from django.db import models

# Create your models here.

class Advertiser(models.Model):
    name = models.CharField(max_length=55) 

    def __str__(self)-> str:
        return self.name

class Demand(models.Model):
    description = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=55)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    status = models.CharField(max_length=55)

    def __str__(self)-> str:
        return self.description