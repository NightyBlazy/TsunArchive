from django.db import models
from PIL import Image


# Create your models here.

class Archive(models.Model):
    name = models.CharField(max_length=200,blank=True)
    gender = models.TextField(blank=True)
    affiliation = models.TextField(blank=True)
    hair_style = models.TextField(blank=True)
    hair_color = models.TextField(blank=True)
    Ttype = models.TextField(blank=True)
    image = models.ImageField(upload_to='characters',default='default.jpg')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 400 or img.width > 400:
            output_size = (400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)