# Generated by Django 3.2.5 on 2021-07-11 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='assets/img/home-bg.jpg', null=True, upload_to='assets/img/'),
        ),
    ]