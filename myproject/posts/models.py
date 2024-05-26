from django.db import models

# Create your models here.

# In Django, data is created in objects, called Models, 
# A Django model is a table in your database.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
