from django.apps import AppConfig as DjangoAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(DjangoAppConfig):
    """
    Configuration entry point for the django_randomprimary app
    """
    label = name = 'django_randomprimary'
    verbose_name = _("django_randomprimary app")
