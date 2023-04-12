from django.db import models

class Post(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField()

   def __str__(self):
       return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    parent     = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    def __str__(self):
        return self.content