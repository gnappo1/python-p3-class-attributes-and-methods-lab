class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        type(self).add_song_to_count()
        type(self).add_to_genres(genre)
        type(self).add_to_artists(artist)

    @classmethod
    def add_to_genres(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        # if genre in cls.genre_count:
        #     cls.genre_count[genre] += 1
        # else:
        #     cls.genre_count[genre] = 1
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
        # if artist in cls.artist_count:
        #     cls.artist_count[artist] += 1
        # else:
        #     cls.artist_count[artist] = 1
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        return cls.count


# problems = Song("99 Problems", "Jay Z", "Rap")
# halo = Song("Halo", "Beyonce", "Pop")
# spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# teen = Song("Smells Like Teen", "Nirvana", "Rock")
print("hello")
