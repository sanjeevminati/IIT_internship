# Generated by Django 3.2.5 on 2021-08-25 05:42

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_image_image'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=main.models.path_and_rename),
        ),
    ]