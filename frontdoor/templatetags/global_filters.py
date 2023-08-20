from django import template
from datetime import datetime

FMT_DATETIME = "%Y-%m-%d %H:%M"
FMT_PRETTY_DATETIME = "%d  %Y %Hh%M"
MONTHS = ['', 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']


register = template.Library()


@register.filter(name='to_datetime')
def to_datetime(value):
    res = "n/a"
    if value:
       m = MONTHS[int(value.strftime("%m"))].title()
       fmt = f"%d {m} %Y %Hh%M"
       res = value.strftime(fmt)
    return res

