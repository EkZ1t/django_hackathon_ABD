from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response 
from .serializers import TrackSerializer, AlbumSerializer, GenreSerializer
from .models import Track, Album, Genre, Like

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.

# функция ответственная за аудиоплеер
def index(request):
    paginator= Paginator(Track.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

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