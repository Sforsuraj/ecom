# Generated by Django 5.0.2 on 2024-03-04 17:25

import ecommerce_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0011_rename_category_name_shop_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_img',
            field=models.ImageField(default='', upload_to=ecommerce_app.models.content_file_name),
        ),
    ]
