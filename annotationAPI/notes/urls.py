
from django.urls import path
from .views import *


urlpatterns = [
    path('', view=list_create_AudioPIVIEW, name="home"),
]