from django.db import models

class Couriers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Consumer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_address1 = models.CharField(max_length=100)
    business_city = models.CharField(max_length=50)
    business_inventory = Business_inventor

class Business_inventory(models.Model):
