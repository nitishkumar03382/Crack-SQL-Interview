from django.apps import AppConfig


class QuestionbankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'questionbank'

    def ready(self):
        import questionbank.signals
