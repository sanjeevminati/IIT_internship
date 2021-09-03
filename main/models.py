from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

User._meta.get_field('email')._unique = True


class Image(models.Model):
    image = models.FileField(max_length=255)