from django.http import HttpResponse
from movies.models import Movie, WatchList
from movies.api.serializers import WatchListSerializer, MoviesSerilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status


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
        # get data from the request --> POST
        # request.Data
        print(request.data)
        # I need to serilize the data
        serlized_movie = MoviesSerilizer(data=request.data)
        if serlized_movie.is_valid():
            serlized_movie.save()

            #id --->
        else:
            print(serlized_movie.errors)

    movies = Movie.objects.all()
    serilized_movies = MoviesSerilizer(movies, many=True)
    return Response(serilized_movies.data)


### retrive, update , delete
@api_view(["GET", "PUT", "DELETE"])
def singleMovieOperations(request, id):
    ### I need to retreive the object from model
    movie = get_object_or_404(Movie, pk=id)
    if request.method == "PUT":
        # put data in the request in the movie object
        serlized_movie = MoviesSerilizer(movie, data=request.data)
        if serlized_movie.is_valid():
            serlized_movie.save()
            return Response(serlized_movie.data)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serlized_movie = MoviesSerilizer(movie)
    return Response(serlized_movie.data)


@api_view()  # assume that method is GET
def getWatchlists(request):
    watchlists = WatchList.objects.all()  # queryset
    # use serializer to convert queryset into json
    watchlists_serialized = WatchListSerializer(watchlists, many=True)
    # return with serialized object ---> property data --->
    return Response(watchlists_serialized.data)
