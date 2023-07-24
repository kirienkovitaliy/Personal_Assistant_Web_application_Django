from django.shortcuts import render, redirect

from .forms import FileForm
from .models import File, gd_storage


def get_files(request):
    files = File.objects.all()
    return render(request, "file_app/files.html", context={"files": files})


def upload_file(request):
    form_class = FileForm

    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        
        if form.is_valid():
            file = form.save(commit=False)
            file.name = request.FILES["file"].name
            file.save()
            return redirect("file_app:files")
        else:
            return render(request, "file_app/upload_file.html", context={"form": form_class})
    return render(request, "file_app/upload_file.html", context={"form": form_class})


def delete_file(request, id):
    file = File.objects.get(id=id)
    file.delete()
    return redirect("file_app:files")

