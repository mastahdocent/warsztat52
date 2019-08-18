from django.urls import path, re_path, include

from api.views import PhotosListView, PhotosDetailView, LoginView

urlpatterns = [
    path("photos/", PhotosListView.as_view(), name="api-photos"),
    path("photos/<int:pk>/", PhotosDetailView.as_view(), name="api-photo"),
    path("login/", LoginView.as_view(), name="api-login"),
]
