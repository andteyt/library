# Generated by Django 4.0.4 on 2022-06-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_books_img_alter_authors_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='img',
            field=models.ImageField(upload_to='static/img/book'),
        ),
    ]
