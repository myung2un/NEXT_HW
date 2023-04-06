from django.db import models

# Create your models here.
class Article(models.Model):
    category = models.CharField(max_length=20, default="취미")
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
