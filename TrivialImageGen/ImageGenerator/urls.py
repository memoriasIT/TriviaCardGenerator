from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='listImages'),
    path('generate/', views.generateImage, name='generateImage'),
    path('<int:id>/', views.image, name='image')
]


