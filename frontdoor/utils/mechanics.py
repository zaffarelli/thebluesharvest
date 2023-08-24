
FONTSET = ['Mukta', 'Oswald', 'Raleway', 'Kalam']


def fetch_articles(titles=[]):
    from frontdoor.models.articles import Article
    selection = Article.objects.filter(title__in=titles)
    return selection