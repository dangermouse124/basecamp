from django.db import models

# Create your models here.
class temp_10min(models.Model):

    sensor_id = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()

    def __str__(self):
        return str(self.temperature) + " DegC at " + str(self.date_time)

class temp_max_min(models.Model):

    sensor_id = models.IntegerField()
    date = models.DateField()
    max = models.IntegerField()
    max_time = models.TimeField()
    min = models.IntegerField()
    min_time = models.TimeField()

    def __str__(self):
        return str(self.sensor_id)

