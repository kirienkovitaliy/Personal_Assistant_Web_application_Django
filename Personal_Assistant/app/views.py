import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from typing import Any, Dict
from .forms import PictureForm
from .models import Picture


@login_required
def main(request: HttpRequest) -> HttpResponse:
    """
    Main view for the web application.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    return render(request, "app/index.html")


@login_required
def upload(request: HttpRequest) -> HttpResponse:
    """
    View to handle the picture upload form.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    form = PictureForm(instance=Picture())
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user
            pic.save()
            return redirect(to="app:pictures")
        print("not valid")
    return render(
        request,
        "app/upload.html",
        context={"title": "Personal_Assistant_Web_application_Django", "form": form},
    )


@login_required
def pictures(request: HttpRequest) -> HttpResponse:
    """
    View to display a user's pictures.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    pictures = Picture.objects.filter(user=request.user).all()
    print(pictures)
    return render(
        request,
        "app/pictures.html",
        context={
            "title": "Personal_Assistant_Web_application_Django",
            "pictures": pictures,
            "media": settings.MEDIA_URL,
        },
    )


@login_required
def remove(request: HttpRequest, pic_id: int) -> HttpResponse:
    """
    View to remove a picture.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pic_id (int): The ID of the picture to be removed.

    Returns:
        HttpResponse: The HTTP response object.
    """
    picture = get_object_or_404(Picture, pk=pic_id, user=request.user)
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(picture.first().path)))
    except OSError as e:
        print(e)
    picture.delete()
    return redirect(to="app:pictures")


@login_required
def edit(request: HttpRequest, pic_id: int) -> HttpResponse:
    """
    View to edit a picture's description.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pic_id (int): The ID of the picture to be edited.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == "POST":
        description = request.POST.get("description")
        Picture.objects.filter(pk=pic_id, user=request.user).update(
            description=description
        )
        return redirect(to="app:pictures")

    picture = get_object_or_404(Picture, pk=pic_id, user=request.user)
    return render(
        request,
        "app/edit.html",
        context={
            "title": "Personal_Assistant_Web_application_Django",
            "pic": picture,
            "media": settings.MEDIA_URL,
        },
    )
