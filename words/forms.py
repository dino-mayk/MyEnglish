from core.forms import AbstractModelForm
from words.models import Word


class AddOrUpdateWordForm(AbstractModelForm):
    class Meta:
        model = Word
        fields = (
            'word_in_english',
            'word_in_russian',
        )
