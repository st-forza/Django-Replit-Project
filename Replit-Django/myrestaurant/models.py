from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=255)




# python manage.py makemigrations
# python manage.py migrate