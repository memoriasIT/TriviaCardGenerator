from django.db import models
from django.utils.timezone import now

class Image(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    #name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField(default=now, primary_key=True)
    #image = models.ImageField(upload_to = 'output/', default = 'output/demo.png')

    def __str__(self):
        return self.name
