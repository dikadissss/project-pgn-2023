# Generated by Django 4.2.6 on 2023-11-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelompok', models.CharField(choices=[('satu', 'I (Satu)'), ('dua', 'II (Dua)'), ('tiga', 'III (Tiga)'), ('empat', 'IV (Empat)'), ('lima', 'V (Lima)')], max_length=50)),
            ],
        ),
    ]
