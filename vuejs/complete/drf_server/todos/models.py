from django.db import models
from django.conf import settings

# models.py 안에서는 user모델 쓸 때 settings.AUTH_USER_MODEL
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)