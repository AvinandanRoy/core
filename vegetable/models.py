from django.db import models

# Create your models here.


class Recipe(models.Model):
    
    recipe_name = models.CharField( max_length= 50 )
    recipe_des = models.TextField()
    recipe_img = models.ImageField( upload_to= 'recip' )