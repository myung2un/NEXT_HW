from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    dday = models.IntegerField(default = 0)

    def __str__(self):
        return self.title