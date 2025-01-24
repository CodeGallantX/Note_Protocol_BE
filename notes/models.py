from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Notes(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notes')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notes')
    messages = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return r"From {self.sender.username} to {self.receiver.username}"