from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateTimeField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField("Genre", related_name='albums')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = "Альбомы"
        ordering = ['uploaded_at']

    def __str__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField("Genre", related_name='tracks')
    
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2
    
    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = "Треки"
        ordering = ['uploaded_at']

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.album})"

class Genre(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    
    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        unique_together = ['user', 'track']

    def __str__(self):
        return f'Liked by {self.user.username}'