from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

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


def delete(request, pk):
    template_name = 'words/delete.html'
    word = get_object_or_404(Word, pk=pk)
    context = {
        'word': word,
    }

    if request.user.id != word.user.id:
        messages.error(request, 'У вас недостаточно прав')
        return redirect('homepage:home')

    if request.POST:
        word.delete()
        messages.success(request, 'Ваше слово успешно удалено')
        return redirect('words:list')

    return render(request, template_name, context)
