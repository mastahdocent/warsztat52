from django import forms

from photoalbum.models import InstaUser, Photo


class UserEditForm(forms.ModelForm):
    class Meta:
        model = InstaUser
        fields = [
            "first_name",
            "last_name",
            "age",
            "avatar"
        ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            "image",
            "description"
        ]
