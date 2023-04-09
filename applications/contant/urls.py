from .views import TrackViewSet, AlbumViewSet, GenreViewSet, index
from rest_framework.routers import DefaultRouter 

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


router = DefaultRouter()
router.register('track', TrackViewSet, 'tracks')
router.register('album', AlbumViewSet, 'albums')
router.register('genre', GenreViewSet, 'genres')


urlpatterns = [
    path("", index, name='index'),
]

urlpatterns += router.urls