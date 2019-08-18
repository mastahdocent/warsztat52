from rest_framework import serializers

from photoalbum.models import Photo, InstaUser


class InstaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "email",
        ]


class InstaUserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaUser
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class PhotoSerializer(serializers.ModelSerializer):
    author = InstaUserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author", 
        queryset=InstaUser.objects.all(),
        write_only=True
    )
    likes = InstaUserMiniSerializer(read_only=True, many=True)

    class Meta:
        model = Photo
        fields = [
            "id",
            "image",
            "width",
            "height",
            "author",
            "author_id",
            "description",
            "likes"
        ]
