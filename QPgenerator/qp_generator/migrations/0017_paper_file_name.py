# Generated by Django 2.0.5 on 2018-06-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qp_generator', '0016_auto_20180612_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='file_name',
            field=models.CharField(default='abc.pdf', max_length=200),
            preserve_default=False,
        ),
    ]
