from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views import View
from django.views.generic.detail import DetailView

from photoalbum.models import Photo, InstaUser
from photoalbum.forms import UserEditForm, PhotoForm


class HomeView(View):
    def get(self, request):
        photos = Photo.objects.all().select_related().prefetch_related("likes")
        form = PhotoForm()
        return render(request, "index.html", {
            "photos": photos,
            "form": form
        })

    def post(self, request):
        form = PhotoForm(data=request.POST, files=request.FILES)
        photo = form.save(commit=False)
        photo.author = request.user
        photo.save()
        return redirect("home")


# class PhotoDetailView(View):
#     def get(self, request, id):
#         # try:
#         #     photo = Photo.objects.get(pk=id)
#         # except Photo.DoesNotExist:
#         #     raise Http404

#         photo = get_object_or_404(Photo, id=id)
#         return render(request, "photo.html", {"photo": photo})

class PhotoDetailView(DetailView):
    model = Photo
    template_name = "photo.html"


class PhotoLikeView(View):
    def post(self, request, id):
        photo = get_object_or_404(Photo, id=id)
        user = request.user

        if user in photo.likes.all():
            photo.likes.remove(user)
        else:
            photo.likes.add(user)

        return redirect("photo", id=photo.id)


class UserDetailView(View):
    def get(self, request, id):
        user = get_object_or_404(InstaUser, pk=id)
        return render(request, "user.html", {"user": user})


class UserEditView(View):
    def get(self, request):
        user = request.user
        form = UserEditForm(instance=user)
        return render(request, "user-edit.html", {"form": form})

    def post(self, request):
        user = request.user
        form = UserEditForm(request.POST, request.FILES, instance=user)
        form.save()
        return redirect("user", id=user.id)
