# Generated by Django 3.2.5 on 2021-07-11 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='static/assets/img/home-bg.jpg', null=True, upload_to='static/assets/img/'),
        ),
    ]
