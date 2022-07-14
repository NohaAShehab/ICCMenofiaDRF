from rest_framework import serializers
from movies.models import Movie, WatchList


class MovieSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        # exclude = ("watchlist", )





class WatchlistSerlizer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"
