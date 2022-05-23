from rest_framework import serializers

from users.models import Users
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'duration', 'online_path', 'email']

    def create(self, validated_data):
        email = validated_data.pop('email', None)
        user = Users.objects.get(email=email)

        instance = Song.objects.create(**validated_data, user=user)
        return instance


class SongDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'duration', 'online_path']
