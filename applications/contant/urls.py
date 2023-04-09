from .views import TrackViewSet, AlbumViewSet, GenreViewSet
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('track', TrackViewSet, 'tracks')
router.register('album', AlbumViewSet, 'albums')
router.register('genre', GenreViewSet, 'genres')

urlpatterns = router.urls