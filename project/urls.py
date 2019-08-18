"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from photoalbum.views import (HomeView, PhotoDetailView, PhotoLikeView,
                              UserDetailView, UserEditView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("photos/<int:pk>/", PhotoDetailView.as_view(), name="photo"),
    path("photos/<int:id>/like/", PhotoLikeView.as_view(), name="photo-like"),
    path("users/<int:id>/", UserDetailView.as_view(), name="user"),
    path("users/edit/", UserEditView.as_view(), name="user-edit"),

    path('__debug__/', include(debug_toolbar.urls)),

    path('api/', include("api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
