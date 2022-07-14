from django.http import HttpResponse
from movies.models import Movie, WatchList
from movies.api.serializers import WatchListSerializer, MoviesSerilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


def test(request):
    return HttpResponse("test")


#
# @api_view(["GET"])
# def getMovies(request):
#     movies = Movie.objects.all()
#     serilized_movies = MoviesSerilizer(movies, many=True)
#     return Response(serilized_movies.data)


# save new movie in the appliction using the api
@api_view(["GET", "POST"])
def getMovies(request):
    if request.method == "POST":
        # ## create new object ---> sent inform of json
        print(request.data)  # watchlist_id
        # 1- get watchlist object
        # watchlistobject = get_object_or_404(WatchList, pk=request.data["watchlist"])
        # print(watchlistobject)
        # request.data["watchlist_id"]= request.data["watchlist"]
        # request.data["watchlist"]=watchlistobject
        serializeMovie = MoviesSerilizer(data=request.data)
        # print()
        # # ## save the object in the database
        if serializeMovie.is_valid():
        # #     print("valid")
            serializeMovie.save()
            return Response(serializeMovie.data)
        # else:
        #     print(serializeMovie.errors)

    movies = Movie.objects.all()
    serilized_movies = MoviesSerilizer(movies, many=True)
    return Response(serilized_movies.data)


# def getWatchlists(request):
#     watchlists = WatchList.objects.all() #queryset
#     # use serializer to convert queryset into json
#     watchlists_serialized = WatchListSerializer(watchlists, many=True)
#     print(list(watchlists_serialized.data))
#     return HttpResponse(watchlists_serialized.data)

@api_view()  # assume that method is GET
def getWatchlists(request):
    watchlists = WatchList.objects.all()  # queryset
    # use serializer to convert queryset into json
    watchlists_serialized = WatchListSerializer(watchlists, many=True)
    # return with serialized object ---> property data --->
    return Response(watchlists_serialized.data)
