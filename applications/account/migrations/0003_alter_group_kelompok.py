# Generated by Django 4.2.6 on 2023-11-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='kelompok',
            field=models.CharField(choices=[('I (Satu)', 'I (Satu)'), ('II (Dua)', 'II (Dua)'), ('III (Tiga)', 'III (Tiga)'), ('IV (Empat)', 'IV (Empat)'), ('V (Lima)', 'V (Lima)')], max_length=50),
        ),
    ]
