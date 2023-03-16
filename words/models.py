from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail

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

    upload = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        verbose_name='картинка',
        help_text='загрузите картинку',
        null=True,
    )

    def __str__(self):
        return self.word_in_english

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '200x200', crop='center', quality=51)

    def img_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет картинки'

    img_tmb.short_description = 'картинка'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    class Meta:
        verbose_name = 'слово'
        verbose_name_plural = 'слова'
