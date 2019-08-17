from django.db import models
from django.contrib.auth.models import AbstractUser


def avatars_upload_path(instance, filename):
    return f"avatars/{instance.id}/{filename}"


def images_upload_path(instance, filename):
    return f"{filename}"


class Photo(models.Model):
    image = models.ImageField(
        upload_to=images_upload_path, width_field="width", height_field="height")
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "InstaUser", on_delete=models.CASCADE, related_name="photos")
    description = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField("InstaUser", related_name="+")


class InstaUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(
        upload_to=avatars_upload_path, null=True, blank=True)

    def __str__(self):
        return self.username
