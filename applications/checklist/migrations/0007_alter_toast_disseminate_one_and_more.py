# Generated by Django 4.2.6 on 2023-12-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_rename_tsp_toast_tsp_one_toast_tsp_two'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toast',
            name='disseminate_one',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='disseminate_two',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='seiscomp_one',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='seiscomp_three',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='seiscomp_two',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='siren_four',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='siren_one',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='siren_three',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='siren_two',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='toast_one',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='toast_two',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='tsp_one',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='tsp_two',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
        migrations.AlterField(
            model_name='toast',
            name='wrs',
            field=models.BooleanField(choices=[(True, 'Ya'), (False, 'Tidak')], default=False),
        ),
    ]