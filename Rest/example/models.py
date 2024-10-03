from django.db import models


# Create your models here.
class Book(models.Model):
    bid = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.IntegerField()
    publish_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
