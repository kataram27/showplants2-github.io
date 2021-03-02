from django.db import models

# Create your models here.
class userdetails(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    address2=models.CharField(max_length=150)
    city=models.CharField(max_length=50)
    phno=models.CharField(max_length=15)
    zip=models.CharField(max_length=10)

    def __str__(self):
        return self.name
