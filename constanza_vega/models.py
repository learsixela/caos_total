from django.db import models


# Create your models here.
class NasaPicture(models.Model):
    def __init__(self, copyright, date, explanation, media_type, service_version, title, url):
        self.copyright = copyright
        self.date = date
        self.explanation = explanation
        self.media_type = media_type
        self.service_version = service_version
        self.title = title
        self.url = url
