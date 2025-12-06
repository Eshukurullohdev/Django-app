from django.db import models
# Create your models here.
# OPP
# data types -- str,int,boolen,float
# fields
# max_length -- uznligi
# pillow --- rasmlarmi olib kelish uchun kerak kutubxona
# max_length

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser

class Tovar(models.Model):
    img = models.ImageField(upload_to='media')
    karta_tolov = models.IntegerField()
    narhi = models.IntegerField()
    tavsifi = models.CharField(max_length=150)

    def __str__(self):
        return self.tavsifi

