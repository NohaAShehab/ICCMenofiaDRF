from django.contrib import admin

# Register your models here.
from movies.models import Movie, WatchList

admin.site.register(Movie)
admin.site.register(WatchList)