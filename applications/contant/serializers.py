from .models import Track, Genre, Album, Like
from rest_framework import serializers


class TrackSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(method_name='likes_counter')
        
    class Meta:
        model = Track
        fields = '__all__'
    
    def likes_counter(self, instance):
        return Like.objects.filter(track=instance).count()
    

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre 
        fields = ['id', 'title']
        

class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = '__all__'
