# Generated by Django 4.2.3 on 2023-07-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0006_remove_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(),
            preserve_default=False,
        ),
    ]