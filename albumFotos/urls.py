from django.urls import path, include
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('foto', FotoViewset)

urlpatterns = [
    path('', home, name="home"),
    path('album/',album, name="album"),
    path('api/', include(router.urls)),
]
