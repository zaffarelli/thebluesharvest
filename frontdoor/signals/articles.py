from django.db.models.signals import pre_save
from django.dispatch import receiver
from frontdoor.models.articles import Article


@receiver(pre_save, sender=Article, dispatch_uid='pre_save_article')
def pre_save_article(sender, instance, **kwargs):
    instance.fix()
