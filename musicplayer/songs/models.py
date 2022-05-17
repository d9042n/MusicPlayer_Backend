import uuid

from django.db import models
# Create your models here.
from users.models import Users


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, default=None, blank=True, null=True)
    artist = models.CharField(max_length=100, default=None, blank=True, null=True)
    album = models.CharField(max_length=100, default=None, blank=True, null=True)
    duration = models.TextField(default=None, blank=True, null=True)
    online_path = models.TextField(default=None, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.title
