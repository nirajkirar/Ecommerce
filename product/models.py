from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='product/my products')
    price = models.FloatField()
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    desc = models.TextField()       # max length not necessary


class SurfItem(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='product/surf')
    price = models.FloatField()
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    desc = models.TextField()       # max length not necessary

class Transaction(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)  ## foreign key to user model
    cat=models.CharField(max_length=40)
    cat_id=models.IntegerField()
    purchased_quan=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    