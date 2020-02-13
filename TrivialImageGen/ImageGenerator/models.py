from django.db import models
from django.utils.timezone import now

class Image(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'static/cards', default = 'static/cards/noName.png')

    def __str__(self):
        return self.name
