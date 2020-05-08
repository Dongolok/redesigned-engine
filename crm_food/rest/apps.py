from django.apps import AppConfig


class TablesConfig(AppConfig):
    name = 'rest'

    def ready(self):
        import rest.signals
