
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Generator and list of images
    path('image/', include('ImageGenerator.urls')),

    # Admin page
    path('admin/', admin.site.urls),

    # Landing (static html basically)
    path('', include('landing.urls')),

    # Authentication views
    # https://docs.djangoproject.com/en/3.0/topics/auth/default/#module-django.contrib.auth.views
    path('accounts/', include('django.contrib.auth.urls')),
]


