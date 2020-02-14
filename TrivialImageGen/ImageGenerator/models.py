from django.db import models
from django.utils.timezone import now

class Image(models.Model):
    name     = models.CharField(max_length=200)
    data     = models.TextField(default="")
    pub_date = models.DateTimeField('date published')
    uploaded = models.BooleanField(default=False)
    image    = models.ImageField(upload_to = 'static/cards', default = 'static/cards/noName.png')
    imageSol = models.ImageField(upload_to = 'static/cards', default = 'static/cards/noName2.png')

    def __str__(self):
        return self.name
