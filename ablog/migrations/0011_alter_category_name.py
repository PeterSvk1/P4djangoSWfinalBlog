# Generated by Django 5.0.7 on 2024-08-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0010_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='starwars', max_length=200),
        ),
    ]
