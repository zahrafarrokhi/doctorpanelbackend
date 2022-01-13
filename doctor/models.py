from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    image = models.ImageField(default="default_profile_image.jpg")
    profession = models.CharField(max_length=30)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    tel = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.f_name} - {self.l_name}'