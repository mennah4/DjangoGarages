from django.db import models


from django.utils import timezone


class Garage(models.Model):
    # garage name is the province
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.id,self.name)




class Car(models.Model):

    garage = models.ForeignKey('Garage',on_delete=models.CASCADE, blank=True)
    color = models.CharField(max_length=100, null=False)
    manufacturer = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    year = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.model,self.manufacturer,self.garage)
