from django.db import models

GENRE_CHOICES = [
    ('rock', 'Rock'),
    ('pop', 'Pop'),
    ('hip_hop', 'Hip hop'),
    ('jazz', 'Jazz'),
    ('classical', 'Classical'),
    ('country', 'Country'),
    ('electronic', 'Electronic'),
    ('reggae', 'Reggae'),
    ('blues', 'Blues'),
    ('metal', 'Metal'),
    ('r_b', 'R&B'),
    ('alternative', 'Alternative'),
    ('folk', 'Folk'),
    ('indie', 'Indie'),
    ('punk', 'Punk'),
    ('disco', 'Disco'),
    ('latin', 'Latin'),
    ('other', 'Other')
]


class User(models.Model):
    name = models.CharField(verbose_name="Имя пользователя", max_length=255)
    email = models.EmailField(verbose_name="Электроная почта", max_length=254, unique=True)
    registration_date = models.DateField(verbose_name="Дата регистрации", auto_now_add=True)
    following_artists = models.ManyToManyField('Artist', related_name='followerslist', blank=True)
    def __str__(self):
        return self.name

    def following_artists_list(self):
        # noinspection PyUnresolvedReferences
        return self.following_artists.all()

class Artist(models.Model):
    name = models.CharField(verbose_name="Имя артиста", max_length=255)
    #image = models.ImageField(upload_to='artists/', verbose_name="Фото артиста", blank=True)
    genre = models.CharField(verbose_name="Жанр", choices=GENRE_CHOICES, max_length=255, default='other')
    most_popular_track = models.CharField(verbose_name="Самый популярный трек", max_length=255)
    biography = models.TextField(verbose_name='Биография', blank=True)
    followers = models.ManyToManyField(User, related_name='followingartists', blank=True)

    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"
        ordering = ['name']

    def __str__(self):
        return self.name

    def follower_count(self):
        # noinspection PyUnresolvedReferences
        return self.followers.all().count()

class Track(models.Model):
    name = models.CharField(verbose_name="Название трека", max_length=255)
    artists = models.ManyToManyField(Artist, related_name='track_artist')
    album = models.ForeignKey('Album', on_delete = models.CASCADE, verbose_name = 'Альбом', null=True, blank=True)
    duration = models.DurationField(verbose_name='Длительность')
    audio = models.FileField(upload_to='tracks/', verbose_name='Аудиофайл')
    release_date = models.DateField(verbose_name="Дата выпуска")
    #image = models.ImageField(upload_to='track_image/',verbose_name='Обложка трека', blank=True)
    explicit = models.BooleanField(verbose_name="Содержит нецензурные слова", default=False)

    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"
        ordering = ['name']

    def str(self):
        return self.name

class Album(models.Model):
    name = models.CharField(verbose_name='Название альбома', max_length=255)
    artists = models.ManyToManyField(Artist, related_name='album_tracks')
    release_date = models.DateField(verbose_name='Дата выпуска')
    #image = models.ImageField(verbose_name='Обложка альбома', upload_to='album_covers/', blank=True)

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ['name']

    def str(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(verbose_name='Название плейлиста', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    tracks = models.ManyToManyField(Track, verbose_name='Треки', related_name='playlists')

    class Meta:
        verbose_name = "Плейлист"
        verbose_name_plural = "Плейлисты"

    def str(self):
        return self.name