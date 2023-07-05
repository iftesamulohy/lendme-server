# Generated by Django 4.0.5 on 2023-07-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lendapp', '0003_alter_item_facebook_alter_item_instagram_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='product_image',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tag',
            field=models.CharField(choices=[('Featured', 'Featured'), ('Latest', 'Latest')], max_length=20),
        ),
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(upload_to='upload'),
        ),
    ]