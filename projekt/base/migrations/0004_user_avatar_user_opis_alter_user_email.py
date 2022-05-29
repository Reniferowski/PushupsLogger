# Generated by Django 4.0.4 on 2022-05-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_user_first_name_remove_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.webp', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='opis',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]