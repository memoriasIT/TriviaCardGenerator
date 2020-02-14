<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Image

=======
#  __________________________________________
# [              -   IMPORTS -               ]
#
# -  IMPORT DJANGO  -
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.conf import settings # static files dirs

from django.utils import timezone

from django.core.files import File

# -  IMPORT MODELS  -
from .models import Image


# -  PRIVATE MODULES  -            ]
import generatorModule

#  __________________________________________
# [              -  INDEX  -                 ]
#
# URL -> /image
# path('', views.index, name='index'),
>>>>>>> e32b6aa47ae50dbdcdf5e704e63ab993dcc4d80a
def index(request):
    imageList = Image.objects.all()
    context   = {
        'image_list': imageList,
    }
    return render(request, 'ImageGenerator/index.html', context)

<<<<<<< HEAD

=======
#  __________________________________________
# [           -  IMAGE BY ID  -              ]
#
# URL -> /image/id
# path('<int:id>/', views.image, name='image')
>>>>>>> e32b6aa47ae50dbdcdf5e704e63ab993dcc4d80a
def image(request, id):
    image = get_object_or_404(Image, pk=id)

    return render(request, 'ImageGenerator/image.html', {'image': image})
<<<<<<< HEAD
=======

#  __________________________________________
# [           -  GENERATE IMG -              ]
#
# URL -> /image/generate
# path('generate/', views.generateImage, name='generateImage'),
def generateImage(request):
    # Generate Images for object
    time = timezone.now() 
    path = str(settings.STATICFILES_DIRS[0]) + "/temp"
    generatorModule.genImageMain(path)

    # Create object in database
    tempImage = Image.objects.create(name=str(time), pub_date=time)
    tempImage.image.save(str(time)+'_0.png', File(open('static/temp_0.png', 'rb')))
    tempImage.imageSol.save(str(time)+'_1.png', File(open('static/temp_1.png', 'rb')))

    return render(request, 'ImageGenerator/image.html', {'image': tempImage})
>>>>>>> e32b6aa47ae50dbdcdf5e704e63ab993dcc4d80a
