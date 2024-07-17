class Song:
    count = 0
    songs = []
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        type(self).add_song_to_count()
        type(self).add_song_to_songs(self)
        type(self).add_to_genres(genre)
        type(self).add_to_artists(artist)
        type(self).add_to_genre_count(genre)
        type(self).add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_song_to_songs(cls, song):
        cls.songs.append(song)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        #! if there is a key for that genre => +1
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        #! if not => = 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        #! if there is a key for that genre => +1
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        #! if not => = 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def max_helper(cls, artist_tup):
        _, count = artist_tup
        return count

    @classmethod
    def max_artist_by_count(cls):
        # walrus operator: variable assignment + conditional statement on the same line
        if max_tuple := max(cls.artist_count.items(), default=None, key=cls.max_helper):
            return max_tuple[0]

# s1 = Song("99 Problems", "Jay Z", "Rap")
# s2 = Song("Halo", "Beyonce", "Pop")
# s2 = Song("Halo", "Beyonce", "Pop")
# s2 = Song("Halo", "Beyonce", "Pop")
# s3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# s4 = Song("ksdbvwdviu", "Nirvana", "Rock")


# min
# max
# sort VS sorted
# list comprehensions for mapping and filtering (place an if at the end of the list comprehension)
# next(gen expression) for finding


print('done')
