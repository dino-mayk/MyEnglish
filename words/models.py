from django.db import models
from users.models import CustomUser


class Word(models.Model):
    user = models.ForeignKey(
        CustomUser(),
        on_delete=models.CASCADE,
        verbose_name='автор',
        help_text='выберете пользователя',
    )

    word_in_russian = models.CharField(
        'слово на русском',
        max_length=150,
    )

    word_in_english = models.CharField(
        'слово на английском',
        max_length=150,
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'слово'
        verbose_name_plural = 'слова'
