# Generated by Django 2.2.24 on 2023-04-30 13:50

from django.db import migrations
from phonenumbers import is_valid_number, parse


def owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()

    for flat in flats.iterator():
        owners_phonenumber = flat.owners_phonenumber
        parsed_number = parse(owners_phonenumber, 'RU')
        if is_valid_number(parsed_number):
            flat.owner_pure_phone = parsed_number
            flat.save()



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_phone_number_field'),
    ]

    operations = [
        migrations.RunPython(owner_pure_phone)
    ]
