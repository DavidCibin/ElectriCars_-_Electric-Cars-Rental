# Generated by Django 3.2.2 on 2021-05-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(help_text='city', max_length=100),
        ),
    ]
