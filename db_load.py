import csv
from datetime import datetime
from songs.models import *


def save_song(line, band, artist):
    print(line)
    song = Song(
        date=line[0],
        # date=datetime.strptime(line[0], '%m/%d/%y %H:%M %p'),
        name=line[1],
        album=line[2],
        band=band,
        artist=artist,
        length=line[6],
        genre=line[7],
        sub_genre=line[8],
        similar_bands=line[9],
        tags=line[10],
        instruments=line[11],
    )
    try:
        song.save()
        print(song.id)
    except Exception as e:
        print('>>>>>>> Error saving song', e)


def load_db():
    with open('prueba_back_monoku_2021_datos.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            try:
                artist_record, created_artist = Artist.objects.get_or_create(name=row[5])
                band_record, created_band = Band.objects.get_or_create(name=row[4])
                save_song(row, band_record, artist_record)
            except Exception as e:
                print('>>>>>>> Error saving band or artist >>>>>>', e)
