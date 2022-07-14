from rest_framework import serializers
from movies.models import Movie


#
# convert complex data into simple native python datatype
# that can be converted to json


class WatchListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    type = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    # backword relation
    movies = serializers.StringRelatedField(many=True, read_only=True)


class MoviesSerilizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    # display where the information of the watchlist contains the movie
    watchlist_id = serializers.IntegerField()
    watchlist = WatchListSerializer(read_only=True)

    def create(self, validated_data):
        add_object = Movie.objects.create(**validated_data)
        print(add_object.id)
        ##
        return add_object

    def update(self, instance, validated_data):
        # get fields I want to update from validated_Data
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.active = validated_data.get("active", instance.active)
        instance.watchlist_id = validated_data.get("watchlist_id", instance.watchlist_id)
        instance.save()
        return instance
