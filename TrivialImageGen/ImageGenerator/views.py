#  __________________________________________
# [              -   IMPORTS -               ]
#
# -  IMPORT DJANGO  -
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

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
def index(request):
    imageList = Image.objects.all()
    context   = {
        'image_list': imageList,
    }
    return render(request, 'ImageGenerator/index.html', context)

#  __________________________________________
# [           -  IMAGE BY ID  -              ]
#
# URL -> /image/id
# path('<int:id>/', views.image, name='image')
def image(request, id):
    image = get_object_or_404(Image, pk=id)

    return render(request, 'ImageGenerator/image.html', {'image': image})

#  __________________________________________
# [           -  GENERATE IMG -              ]
#
# URL -> /image/generate
# path('generate/', views.generateImage, name='generateImage'),
@login_required()
def generateImage(request):
    # required data
    time = timezone.now() 
    path = str(settings.STATICFILES_DIRS[0]) + "/temp"
    
    # Generate image and save data from it
    imageData = generatorModule.genImageMain(path)

    print(imageData)

    # Create object in database
    tempImage = Image.objects.create(name=str(time), pub_date=time, data=str(imageData))
    tempImage.image.save(str(time)+'_0.png', File(open('static/temp_0.png', 'rb')))
    tempImage.imageSol.save(str(time)+'_1.png', File(open('static/temp_1.png', 'rb')))


    return render(request, 'ImageGenerator/image.html', {'image': tempImage})
