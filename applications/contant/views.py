from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response 
from .serializers import TrackSerializer, AlbumSerializer, GenreSerializer
from .models import Track, Album, Genre, Like

# Create your views here.

class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    
    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        track = self.get_object()
        like = Like.objects.filter(user=request.user, track=track)
        if like.exists():
            like.delete()
            return Response({'Liked': False})
        else: 
            Like.objects.create(user=request.user, track=track).save()
            return Response({'Liked': True})
    
class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer