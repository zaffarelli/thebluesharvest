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
    from frontdoor.utils.mechanics import populate_gallery
    populate_gallery('pictures/dates/')
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

    # all_concerts = Concert.objects.all().order_by('-perf_date').filter(perf_date__lte=datetime.now)
    context['articles'] = all_articles
    # context['concerts'] = all_concerts
    return render(request, 'frontdoor/presentation.html', context=context)


def concerts(request):
    context = prepare_index(request)
    from frontdoor.models.articles import Article
    from frontdoor.models.concerts import Concert
    all_articles = Article.objects.all()
    now = datetime.now()
    future_concerts = Concert.objects.all().order_by('-perf_date').filter(perf_date__gt=now)
    then2023 = datetime(year=2022, month=12, day=31)
    concerts = Concert.objects.all().order_by('-perf_date').filter(perf_date__lte=now, perf_date__gt=then2023)
    concerts_2022 = Concert.objects.all().order_by('-perf_date').filter(perf_date__lte=then2023)
    context['articles'] = all_articles
    context['concerts'] = concerts
    context['past_concerts'] = concerts_2022
    context['future_concerts'] = future_concerts
    return render(request, 'frontdoor/concerts.html', context=context)


def medias(request):
    from frontdoor.models.gallery_items import GalleryItem
    context = prepare_index(request)
    pix = GalleryItem.objects.all()
    all_pictures = []
    for pic in pix:
        content = pic.generate_crop()
        all_pictures.append(
            {'ref': pic.image_reference, "cropped": f"{pic.image_path}thumbnails/crop_{pic.image_short}"})
    context['pictures'] = all_pictures
    return render(request, 'frontdoor/medias.html', context=context)


def home(request):
    context = prepare_index(request)
    from frontdoor.utils.mechanics import fetch_articles
    articles = ["Pitch Principal", "Citation du pitch"]
    context['articles'] = fetch_articles(articles)
    return render(request, 'frontdoor/home.html', context=context)


def compositions(request):
    context = prepare_index(request)
    return render(request, 'frontdoor/compositions.html', context=context)


def music(request):
    context = prepare_index(request)
    return render(request, 'frontdoor/music.html', context=context)


def videos(request):
    context = prepare_index(request)
    return render(request, 'frontdoor/videos.html', context=context)


def contacts(request):
    context = prepare_index(request)
    return render(request, 'frontdoor/contacts.html', context=context)
