# Generated by Django 2.0.5 on 2018-06-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qp_generator', '0017_paper_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='date',
            field=models.CharField(default='12-06-2018', max_length=30),
            preserve_default=False,
        ),
    ]
