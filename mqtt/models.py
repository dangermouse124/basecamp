from django.db import models
from django.utils.timezone import localtime


# Create your models here.
class temp_10min(models.Model):

    sensor_id = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()

    def __str__(self):
        formatedDate = (localtime(self.date_time)).strftime("%H:%M %d-%b-%Y")
        return str(self.temperature) + " DegC at " + str(formatedDate)

class temp_max_min(models.Model):

    sensor_id = models.IntegerField()
    date = models.DateField()
    max = models.IntegerField()
    max_time = models.TimeField()
    min = models.IntegerField()
    min_time = models.TimeField()

    def __str__(self):
        formatedDate = (self.date).strftime("%d-%b-%Y")
        return str(formatedDate)

class door_status(models.Model):
    Timestamp = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=50)

    def __str__(self):
        formatedDate = (self.Timestamp).strftime("%H:%M:%S %d-%b-%Y")
        return str(self.Status) + " at " + str(formatedDate)
