# Generated by Django 3.2.5 on 2021-09-01 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210901_1233'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Caption',
        ),
        migrations.AddField(
            model_name='image',
            name='caption_1',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='caption_2',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='caption_3',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='caption_4',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='caption_5',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
