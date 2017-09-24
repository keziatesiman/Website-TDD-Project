from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=27)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
