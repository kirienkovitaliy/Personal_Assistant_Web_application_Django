from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests

from .forms import FileForm
from .models import File
from .utils.get_category import get_category


@login_required
def delete_file(request, id):
    file = File.objects.get(id=id)
    file.delete()
    return redirect("file_app:files")


@login_required
def download_file(request, id):
    file = File.objects.get(id=id)
    file_url = file.file.url
    response = requests.get(file_url)

    if response.status_code == 200:

        file_content = response.content
        response = HttpResponse(file_content, 
                                headers={
                                    "content_type": "application/octet-stream",
                                    "Content-Disposition": f"attachment; filename={file.name}"
                                    })
        return response
    return HttpResponse("Something was wrong")


@login_required
def get_audio_files(request):
    files = File.objects.filter(category="audio")
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def get_documents_files(request):
    files = File.objects.filter(category="document")
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def get_files(request):
    files = File.objects.all()
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def get_image_files(request):
    files = File.objects.filter(category="image")
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def get_other_files(request):
    files = File.objects.filter(category="other")
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def get_video_files(request):
    files = File.objects.filter(category="video")
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def search_files(request):
    files = File.objects.all()
    if request.method == "POST":
        keyword = request.POST["keyword"]
        files = File.objects.filter(name__icontains=keyword)
        return render(request, "file_app/files.html", context={"files": files})
    return render(request, "file_app/files.html", context={"files": files})


@login_required
def upload_file(request):
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
            return render(request, "file_app/upload_file.html", context={"form": form_class})
    return render(request, "file_app/upload_file.html", context={"form": form_class})

