# Generated by Django 4.0.4 on 2022-05-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='imie',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nazwisko',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='opis',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
