from django.db import models

# Create your models here.
class User(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Video(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    file = models.FileField(upload_to='videos')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title 