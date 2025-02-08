from django.db import models


# Create your models here.

class Links(models.Model):
    
    def __str__(self):
        return self.name if self.name else "No Name"
    
    address = models.CharField(max_length=500,null=True,blank=True)
    name = models.CharField(max_length=500,blank=True,null=True)
    
