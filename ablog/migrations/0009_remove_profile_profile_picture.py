# Generated by Django 5.0.7 on 2024-07-22 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0008_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
    ]
