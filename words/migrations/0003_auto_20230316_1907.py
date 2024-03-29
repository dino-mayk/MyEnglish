# Generated by Django 3.2.4 on 2023-03-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_wordimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='photo',
            field=models.ImageField(help_text='загрузите картинку', null=True, upload_to='uploads/preview/%Y/%m', verbose_name='картинка'),
        ),
        migrations.DeleteModel(
            name='WordImage',
        ),
    ]
