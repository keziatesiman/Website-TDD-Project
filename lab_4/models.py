from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    def convertTimezone():
        return timezone.now() + timezone.timedelta(hours=7)


    name = models.CharField(max_length=27)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(default=convertTimezone)

    def __str__(self):
        return self.message
