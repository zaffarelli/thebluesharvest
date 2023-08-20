from django.shortcuts import render
from datetime import datetime
from frontdoor.utils.mechanics import FONTSET


def prepare_index(request):
    d = datetime.now()
    context = {'fontset': FONTSET}
    return context


def index(request):
    context = prepare_index(request)
    return render(request, 'frontdoor/index.html', context=context)


def demo(request):
    context = prepare_index(request)
    from frontdoor.models.articles import Article
    from frontdoor.models.concerts import Concert
    all_articles = Article.objects.all()
    all_concerts = Concert.objects.all().order_by('-perf_date')
    context['articles'] = all_articles
    context['concerts'] = all_concerts
    return render(request, 'frontdoor/demo.html', context=context)


def presentation(request):
    context = prepare_index(request)
    from frontdoor.models.articles import Article
    from frontdoor.models.concerts import Concert
    all_articles = Article.objects.all()
    all_concerts = Concert.objects.all().order_by('-perf_date')
    context['articles'] = all_articles
    context['concerts'] = all_concerts
    return render(request, 'frontdoor/presentation.html', context=context)


def concerts(request):
    context = prepare_index(request)
    from frontdoor.models.articles import Article
    from frontdoor.models.concerts import Concert
    all_articles = Article.objects.all()
    all_concerts = Concert.objects.all().order_by('-perf_date')
    context['articles'] = all_articles
    context['concerts'] = all_concerts
    return render(request, 'frontdoor/concerts.html', context=context)


def medias(request):
    context = prepare_index(request)
    all_pictures = []
    for x in range(5):
        all_pictures.append({'ref':f'frontdoor/pictures/bh{x+1}.jpg'})
    context['pictures'] = all_pictures
    return render(request, 'frontdoor/medias.html', context=context)
