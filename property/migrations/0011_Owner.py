# Generated by Django 2.2.24 on 2023-05-02 06:25

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230430_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='address',
            field=models.ManyToManyField(related_name='problem', to='property.Flat', verbose_name='Адрес квартиры'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Допустимый номер телефона'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Допустимый номер телефона')),
                ('addresses', models.ManyToManyField(related_name='apartments', to='property.Flat', verbose_name='Квартиры владельца')),
            ],
        ),
    ]
