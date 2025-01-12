# Generated by Django 2.2.24 on 2023-05-02 06:41

from django.db import migrations


def data_transport(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()

    for flat in flats.iterator():
        owner_obj, status = Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone,
        )
        if status:
            owner_obj.addresses.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_Owner'),
    ]

    operations = [
        migrations.RunPython(data_transport)
    ]
