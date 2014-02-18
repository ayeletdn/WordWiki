from django.shortcuts import render, get_object_or_404, redirect
from pages.forms import NewWikiPage

from pages.models import Page


def index(request):
    words_list = Page.objects.all()
    context = {'word_list': words_list}
    return render(request, 'pages/index.html', context)


def detail(request, word):
    page = get_object_or_404(Page, word=word)
    return render(request, 'pages/detail.html', {'page': page})


def new(request):
    if request.method == "POST":
        f = NewWikiPage(request.POST)
        if f.is_valid():
            page = f.save()
            return redirect(page)  # get absolute

    else:
        f = NewWikiPage()

    return render(request, 'pages/new.html', {
        'form': f
    })