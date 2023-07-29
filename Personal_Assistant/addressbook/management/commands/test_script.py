from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from addressbook.models import Contact


class Command(BaseCommand):
    help = "My custom script to work with models"

    def handle(self, *args, **kwargs):
        # Your custom script logic here
        contacts = Contact.objects.all()
        print(type(contacts))
        filtered_contacts = []
        for obj in contacts:
            print(obj.name, obj.birthday)
            start_date = now().date()
            end_date = start_date + timedelta(days=7)
            if not obj.birthday:
                continue
            birthday = obj.birthday.replace(year=start_date.year)
            if start_date <= birthday < end_date:
                filtered_contacts.append(obj.pk)
                print("in list")
            print("-" * 50)
        result = Contact.objects.filter(pk__in=filtered_contacts)
        for r in result:
            print(r.name, r.birthday)
