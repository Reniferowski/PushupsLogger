# Generated by Django 4.0.4 on 2022-06-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_user_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dzien',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='limit',
            field=models.BooleanField(default=False),
        ),
    ]
