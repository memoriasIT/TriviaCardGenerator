from django.db import models
from django.utils.timezone import now

class Image(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'static/cards', default = 'static/cards/noName.png')
=======
    name     = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image    = models.ImageField(upload_to = 'static/cards', default = 'static/cards/noName.png')
    imageSol = models.ImageField(upload_to = 'static/cards', default = 'static/cards/noName2.png')
>>>>>>> e32b6aa47ae50dbdcdf5e704e63ab993dcc4d80a

    def __str__(self):
        return self.name
