# Generated by Django 4.2.3 on 2023-07-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addressbook", "0003_alter_contact_address_alter_contact_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone_number",
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
