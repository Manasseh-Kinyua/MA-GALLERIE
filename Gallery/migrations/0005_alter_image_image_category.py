# Generated by Django 4.0.3 on 2022-03-27 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0004_image_image_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gallery.location'),
        ),
    ]
