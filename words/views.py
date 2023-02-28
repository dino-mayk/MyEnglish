from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from core.models import update_attrs
from words.forms import AddOrUpdateWordForm
from words.models import Word


def list(request):
    template_name = 'words/list.html'
    words = Word.objects.filter(user=request.user)
    context = {
        'words': words,
    }
    return render(request, template_name, context)


def add(request):
    form = AddOrUpdateWordForm(request.POST)
    template_name = 'words/add_or_edit.html'
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


def edit(request, pk):
    template_name = 'words/add_or_edit.html'
    word = get_object_or_404(Word, pk=pk)
    form = AddOrUpdateWordForm(
        data=request.POST or None,
        instance=word,
    )
    context = {
        'form': form,
    }

    if request.user.id != word.user.id:
        messages.error(request, 'У вас нет доступа к чужому слову')
        return redirect('homepage:home')

    if request.method == 'POST' and form.is_valid():
        update_attrs(word, **form.cleaned_data)
        messages.success(request, 'Слово было успешно изменено')
        return redirect('words:list')

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
