from django.db import models
from django.contrib.auth.models import User
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission 

permission =  GoogleDriveFilePermission(GoogleDrivePermissionRole.READER,
                                                                 GoogleDrivePermissionType.USER,
                                                                 "personal.assistant.python.web@gmail.com")
gd_storage = GoogleDriveStorage(permissions=(permission, ))


class File(models.Model):
    name = models.CharField()
    file = models.FileField(storage=gd_storage)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self):
        self.file.delete()
        super().delete()

