# Generated by Django 2.0.5 on 2018-05-18 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qp_generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='Subject_name',
            new_name='subject_name',
        ),
    ]
