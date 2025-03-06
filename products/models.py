from django.db import models

class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True

class Category(BaseModel):

    def __str__(self):
        return self.name

class Product(BaseModel):
    price = models.FloatField()
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
