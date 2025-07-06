from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    enrollment_status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
#updated by ahmad mkhaiber


