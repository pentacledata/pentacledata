from django.db import models
from django.contrib.postgres.fields import ArrayField


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.BooleanField(default=False)


class Schedule(models.Model):
    doctor_name = models.CharField(max_length=50)
    available_days = models.CharField(max_length=50)
    available_time = models.CharField(max_length=50)
    per_patient_time = models.CharField(max_length=50)
    serial_visibility = models.CharField(max_length=50)
    status = models.BooleanField(default=False)


class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)

