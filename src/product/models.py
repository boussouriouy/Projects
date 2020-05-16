from django.db import models
from django.urls import reverse
# Create your models here.
class Cart(models.Model):
     title = models.CharField(max_length= 50)
     price = models.DecimalField(max_digits=100, decimal_places=2)
     description = models.TextField(blank=True)
     summary = models.TextField(blank= False, default= 'This cool!')

     def get_absolute_url(self):
          return reverse("product:list_items", kwargs={'id': self.id}) #this is the nice and cleaner way to link urls