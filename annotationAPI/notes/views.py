
from rest_framework import generics, permissions
from rest_framework.response import Response
import rest_framework.status as status
from .models import *
from .serializers import *



class HomeAPIView(generics.ListCreateAPIView):
    '''
        View: get, post Audio
        liste des audio annoter par l'utilisateur et non par l'utilisateur
    '''
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
list_create_AudioPIVIEW = HomeAPIView.as_view()


class RetUpdateDelHome(generics.RetrieveUpdateDestroyAPIView):
    '''
        View pour put, patch, delete des Audio 
    '''
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_AudioView = RetUpdateDelHome.as_view()


class EmotionAPICview(generics.ListCreateAPIView):
    pass

class AnnotationAPIView(generics.ListCreateAPIView):
    pass
