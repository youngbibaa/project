from rest_framework import serializers
from .models import Actor, Movie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many = True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"