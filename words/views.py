from django.shortcuts import redirect, render

from words.forms import AddWordForm
from words.models import Word


def list(request):
    template_name = 'words/list.html'
    words = Word.objects.filter(user=request.user)
    context = {
        'words': words,
    }
    return render(request, template_name, context)


def add(request):
    form = AddWordForm(request.POST, request.FILES)
    template_name = 'words/add.html'
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        cleaned_data = form.cleaned_data
        word = Word.objects.create(
            user=request.user,
            **cleaned_data
        )
        word.save()

        return redirect('homepage:home')

    return render(request, template_name, context)
