
# here I will register the api-urls
from django.urls import path
from movies.api.views import test, getMovies, getWatchlists
from movies.api.api_views import MovieAPIListView, SingleMovieDetailedView,\
    WatchListListAPIVIEW, WatchListDetailedView

urlpatterns = [
    # path("testpath", test, name="testpath"),
    # path("index", getMovies, name="moviesIndex"),
    # path("watchlist/index", getWatchlists, name="watchlistindex")
    path("index", MovieAPIListView.as_view()),
    path("<int:id>", SingleMovieDetailedView.as_view()),
    path("watchlist/index", WatchListListAPIVIEW.as_view()),
    path("watchlist/<int:watch>", WatchListDetailedView.as_view()),




]
