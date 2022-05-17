import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from musicplayer.utils import Utils

util_function = Utils()


# Create your models here.
class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=50, null=True, blank=True, default=None)
    birthdate = models.CharField(max_length=50, null=True, blank=True, default=None)
    country = models.CharField(max_length=50, null=True, blank=True, default=None)
    user_id = models.CharField(max_length=12, null=False, blank=False, default=util_function.user_id_generator())
    active_token = models.CharField(max_length=6, null=True, blank=True, default=util_function.active_token_generator())

    refresh_token = models.TextField(null=True, blank=True, default=None)
    is_online = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def str(self):
        return "%s" % self.email

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.user_id:
            self.user_id = util_function.user_id_generator()
        super(Users, self).save(force_insert, force_update, using, update_fields)
