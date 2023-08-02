from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
import requests

from .forms import FileForm
from .models import File
from .utils.get_category import get_category
from typing import Any


@login_required
def delete_file(request, id: int) -> Any:
    """
    View function to delete a file with the specified id belonging to the current user.

    Parameters:
        request (HttpRequest): The HTTP request object.
        id (int): The id of the file to delete.

    Returns:
        redirect: Redirects to the 'files' page after successful deletion.
    """
    file = get_object_or_404(File, id=id, user=request.user)
    file.delete()
    return redirect("file_app:files")


@login_required
def download_file(request, id: int) -> Any:
    """
    View function to download a file with the specified id belonging to the current user.

    Parameters:
        request (HttpRequest): The HTTP request object.
        id (int): The id of the file to download.

    Returns:
        HttpResponse: The file content as a downloadable attachment.
    """
    file = get_object_or_404(File, id=id, user=request.user)
    file_url = file.file.url
    response = requests.get(file_url)
    print(response.headers)
    if response.status_code == 200:
        file_content = response.content
        response = HttpResponse(
            file_content,
            headers={
                "Content-Disposition": f"attachment; filename={file.name}",
            },
        )
        return response
    return HttpResponse("Something was wrong")


@login_required
def get_category_files(request, category) -> Any:
    """
    View function to get all audio files uploaded by the current user.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        render: Renders the 'files.html' template with the audio files as context data.
    """
    files = File.objects.filter(category=category, user=request.user)
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def get_files(request) -> Any:
    """
    View function to get all files uploaded by the current user.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        render: Renders the 'files.html' template with all files as context data.
    """
    files = File.objects.filter(user=request.user)
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def search_files(request) -> Any:
    """
    View function to search for files uploaded by the current user based on keyword.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        render: Renders the 'files.html' template with the search results as context data.
    """
    files = File.objects.filter(user=request.user)
    if request.method == "POST":
        keyword = request.POST["keyword"]
        files = File.objects.filter(name__icontains=keyword, user=request.user)
        return render(request, "file_app/files.html", context={"files": files})
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def upload_file(request) -> Any:
    """
    View function to upload a new file for the current user.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        render or redirect: Renders the 'upload_file.html' template for GET request or
        redirects to the 'files' page after successful file upload for POST request.
    """
    form_class = FileForm

    if request.method == "POST":
        form = form_class(request.POST, request.FILES)

        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.name = request.FILES["file"].name
            file.category = get_category(request.FILES["file"].name)
            file.save()
            return redirect("file_app:files")
        else:
            return render(
                request, "file_app/upload_file.html", context={"form": form_class}
            )
    return render(request, "file_app/upload_file.html", context={"form": form_class})
