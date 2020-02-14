from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Image

import generatorModule

def index(request):
    imageList = Image.objects.all()
    context   = {
        'image_list': imageList,
    }
    return render(request, 'ImageGenerator/index.html', context)


def image(request, id):
    image = get_object_or_404(Image, pk=id)

    return render(request, 'ImageGenerator/image.html', {'image': image})


def generateImage(request):
    generatorModule.genImageMain("test")

    return HttpResponse("Maybe Worked")
