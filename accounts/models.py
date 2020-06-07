from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, blank=True)
    picture = models.FileField(upload_to='pictures/%Y/%m/%d/', blank=True)
    member = models.BooleanField(default=False)
