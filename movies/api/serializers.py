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
    # send movies in each watchlist
    # movies = serializers.StringRelatedField(many=True)


class MoviesSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    # watchlist --->
    watchlist = WatchListSerializer()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    # use the serilizer to save the data
    def create(self, validated_data):
        print(validated_data)
        # validated_data.watchlist =
        return Movie.objects.create(**validated_data)
