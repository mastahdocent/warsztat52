from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token

from api.serializers import PhotoSerializer, InstaUser
from photoalbum.models import Photo


# class PhotosListView(views.APIView):
#     def get(self, request):
#         photos = Photo.objects.all()
#         serializer = PhotoSerializer(photos, many=True)
#         return Response(serializer.data)

class LoginView(views.APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        try:
            user = InstaUser.objects.get(username=username)
        except InstaUser.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user_id": user.id,
                "key": token.key
            })
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class PhotosListView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]


class PhotosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]
