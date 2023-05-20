from django.db import models


# Create your models here.
class Product(models.Model):

    name=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to='Product_image')

    def __str__(self):
        return self.name
    

class Collection(models.Model):

    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='Product_image')
    name1=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Shopping(models.Model):
    LANG_CHOICES = (
        ('eng', 'English'),
        ('mal', 'Malayalam'),
        ('ara', 'Arabic'),
    )
    language = models.CharField(max_length=3, choices=LANG_CHOICES)
    author=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.FloatField()
    year=models.IntegerField()
    image=models.ImageField(upload_to="")

    def __str__(self):
        return self.name
    
    

    

class Product(models.Model):
    LANG_CHOICES = (
        ('eng', 'English'),
        ('mal', 'Malayalam'),
        ('ara', 'Arabic'),
    )
    language = models.CharField(max_length=3, choices=LANG_CHOICES)
    author=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.FloatField()
    year=models.IntegerField()
    image=models.ImageField(upload_to="")




