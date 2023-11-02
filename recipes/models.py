from django.db import models


class Recipe(models.Model):
    # define attributes of the class
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text="in minutes")
    ingredients = models.CharField(
        max_length=400, help_text="Ingredients must be seperated by commas"
    )
    difficulty = models.CharField(max_length=20)
    description = models.TextField(max_length=600, help_text="600 character limit")
    pic = models.ImageField(upload_to="recipes", default="empty_bowl.jpg")

    # define string representation od the class
    def __str__(self):
        return str(self.name)
