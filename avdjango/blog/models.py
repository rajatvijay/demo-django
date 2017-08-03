from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Comment(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

# Post.objects.all()
# Post.objects.filter(title='Rajat is an awesome teacher')