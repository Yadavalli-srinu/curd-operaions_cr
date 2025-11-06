from django.db import models

class employee_model(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    mobile = models.BigIntegerField()
    email = models.EmailField()
    salary = models.FloatField()
    dept = models.CharField()
    join_date = models.DateField()
