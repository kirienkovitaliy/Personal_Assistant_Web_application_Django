# Generated by Django 4.2.3 on 2023-07-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addressbook", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="address",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="birthday",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone_number",
            field=models.CharField(max_length=15, null=True),
        ),
    ]
