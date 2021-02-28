from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=250)


class Band(models.Model):
    name = models.CharField(max_length=250)


class Song(models.Model):
    date = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    album = models.CharField(max_length=250)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    length = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    sub_genre = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    instruments = models.CharField(max_length=250)
    similar_bands = models.CharField(max_length=250)
