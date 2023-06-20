# Generated by Django 4.2.2 on 2023-06-20 09:24

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to=myapp.models.user_directory_path, verbose_name=''),
        ),
    ]
