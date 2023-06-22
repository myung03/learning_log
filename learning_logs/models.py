from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Topic that a user is learning about"""
    text = models.CharField(max_length=200)
    stamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Return string representation of model"""
        return self.text

class Entry(models.Model):
    """Entry for a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self): 
        """Return a string representation of model"""
        if len(self.text) < 50:
            return self.text
        else: 
            return f"{self.text[:50]}..."    