from django.contrib import admin

from words.models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'word_in_russian',
        'word_in_english',
    )
