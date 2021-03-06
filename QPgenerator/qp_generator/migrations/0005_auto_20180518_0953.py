# Generated by Django 2.0.5 on 2018-05-18 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qp_generator', '0004_auto_20180518_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=100)),
                ('answer_text', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='match')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qp_generator.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qp_generator.Question'),
        ),
    ]
