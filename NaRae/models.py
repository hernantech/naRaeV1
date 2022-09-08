from django.db import models

class Couriers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    active_job = active_job()


class Consumer(models.Model):
    GUID = models.IntegerField(max_length=50) #GUID is the global user ID, i.e. unique identifier
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def get_location(self, int):
        print("this is where we get the location, either via location services or via the home address that they enter")
    #def location_changed():
    #   a function that handles a change of address midway through the delivery, due to user error, etc

class Business(models.Model):
    business_GUID = models.IntegerField(max_length=50)
    business_name = models.CharField(max_length=100)
    business_address1 = models.CharField(max_length=100)
    business_city = models.CharField(max_length=50)
    def cancel_order(self, ):
        print("thing")
    #business_inventory = Business_inventory.get_item(business_GUID)
    #
    #the above function instantiates the business inventory

class Business_inventory(models.Model):
    item_guid = models.IntegerField(max_length=100)
    def get_item(Business_GUID, item_name: item_guid):
        print(Business_GUID, item_name)


class active_job:
    def __init__(self):
        self.active = "code goes here for creating a job"
