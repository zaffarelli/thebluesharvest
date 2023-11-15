from django.apps import AppConfig


class FrontdoorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frontdoor'

    def ready(self):
        import frontdoor.signals.pages
        import frontdoor.signals.articles