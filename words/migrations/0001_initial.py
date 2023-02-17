# Generated by Django 3.2 on 2023-02-17 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_in_russian', models.CharField(max_length=150, verbose_name='слово на русском')),
                ('word_in_english', models.CharField(max_length=150, verbose_name='слово на английском')),
                ('user', models.ForeignKey(help_text='выберете пользователя', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'слово',
                'verbose_name_plural': 'слова',
            },
        ),
    ]
