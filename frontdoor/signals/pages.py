from django.db.models.signals import pre_save
from django.dispatch import receiver
from frontdoor.models.pages import Page


@receiver(pre_save, sender=Page, dispatch_uid='pre_save_page')
def pre_save_page(sender, instance, **kwargs):
    instance.fix()
