from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
=======
    path('generate/', views.generateImage, name='generateImage'),
>>>>>>> e32b6aa47ae50dbdcdf5e704e63ab993dcc4d80a
    path('<int:id>/', views.image, name='image')
]


