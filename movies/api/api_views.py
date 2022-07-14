from movies.models import Movie, WatchList

from movies.api.modelserilizer import MovieSerilizer, WatchlistSerlizer

from rest_framework import generics


# handle , operations ---> models

class MovieAPIListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerilizer


# update, view single movie , delete movie

class SingleMovieDetailedView(generics.RetrieveUpdateDestroyAPIView):
    # reterive -==> Show,
    # destory ---> delete
    # update ---> update
    serializer_class = MovieSerilizer
    queryset = Movie.objects.all()
    lookup_url_kwarg = 'id'


#################### class based views --> watchlist


class WatchListListAPIVIEW(generics.ListCreateAPIView):
    # implement for 2 methods
    queryset = WatchList.objects.all()
    serializer_class = WatchlistSerlizer

    # get

    # post
    pass


class WatchListDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchlistSerlizer
    lookup_url_kwarg = "watch"
