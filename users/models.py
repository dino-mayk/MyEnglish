from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail

from users.managers import UserManager


class CustomUser(AbstractUser):
    username = models.CharField('имя пользователя', max_length=150)
    email = models.EmailField('email', unique=True)
    avatar = models.ImageField(
        upload_to='uploads/avatars/%Y/%m',
        verbose_name='аватар',
        help_text='загрузите картинку',
        default='default_user_avatar.png',
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]
    objects = UserManager()

    @property
    def get_img(self):
        return get_thumbnail(self.avatar, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.avatar:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'превьюшки'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return f'{self.email}'
