from django.db import models

class Drink(models.Model):
    spirit = models.CharField(max_length=100)
    description = models.TextField()
    photo_url = models.TextField()
    
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipes')


    def __str__(self):
        return self.spirit

class Recipe(models.Model):
    spirit = models.ForeignKey(Drink,  on_delete=models.CASCADE, related_name='drinks') 
    name = models.CharField(max_length=100, null=True)
    recipe = models.TextField() 
    photo_url = models.TextField(null=True)  
 
    def __str__(self):
        return self.recipe

class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.body
    

