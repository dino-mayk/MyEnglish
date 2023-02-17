from django.shortcuts import render

from words.models import Word


def list(request):
    template_name = 'words/list.html'
    words = Word.objects.filter(user=request.user)
    context = {
        'words': words,
    }
    return render(request, template_name, context)
