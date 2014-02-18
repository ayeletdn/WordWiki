from django.shortcuts import render, get_object_or_404

from pages.models import Page


def index(request):
    words_list = Page.objects.all()
    context = {'word_list': words_list}
    return render(request, 'pages/index.html', context)


def detail(request, pk):
    page = get_object_or_404(Page, word=pk)
    return render(request, 'pages/detail.html', {'page': page})

