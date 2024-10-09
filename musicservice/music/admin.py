from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'registration_date')
    search_fields = ('name', 'email')


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'most_popular_track', 'follower_count')
    search_fields = ('name', 'genre')
    list_filter = ('name',)


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'duration', 'explicit')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date')
    search_fields = ('name',)


@admin.register(models.Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)
    list_filter = ('user',)

    def tracks_list(self, obj):
        """Получить список треков в плейлисте."""
        return ", ".join([track.name for track in obj.tracks.all()])

    tracks_list.short_description = 'Треки'

    list_display = ('name', 'user', 'tracks_list')