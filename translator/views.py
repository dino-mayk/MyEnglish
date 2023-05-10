from django.shortcuts import render
from googletrans import Translator


def index(request):
    if request.method == 'POST':
        try:
            lang = request.POST.get('lang', None)
            txt = request.POST.get('txt', None)

            translator = Translator()
            tr = translator.translate(txt, dest=lang)
        except Exception:
            return render(request, 'translator/translator.html')

        return render(
            request,
            'translator/translator.html',
            {'result': tr.text},
        )

    return render(request, 'translator/translator.html')
