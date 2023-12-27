from django.db import models

# Create your models here.
class dress(models.Model):
    name=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class electronic(models.Model):
    name=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
class jewellery(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
