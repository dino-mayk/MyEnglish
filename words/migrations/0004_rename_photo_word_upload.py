# Generated by Django 3.2.4 on 2023-03-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20230316_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='photo',
            new_name='upload',
        ),
    ]
