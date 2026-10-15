from django.db import models

# Create your models here
class Member(models.Model):
     name = models.CharField(max_length: 255)
     role = models.CharField(max_length : 255)
     joined_at = models.DateTimeField(auto_now_add=True)
     def __string__ (self) :
          return self.name