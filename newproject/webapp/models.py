from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name
