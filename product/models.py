from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# from sqlalchemy import null


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    search_tags = models.TextField(blank=True,null=True)
    available = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    favorite = models.ManyToManyField(User,related_name='product_favorite')
    
    def total_favorite(self):
        return self.favorite.count()

    def __str__(self):
        return f'({self.id}-{self.name} - {self.category})'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " "
        return url

class popularProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'