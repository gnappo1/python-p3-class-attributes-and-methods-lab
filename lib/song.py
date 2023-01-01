class Song:
    songs = []
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        self.add_song(name)
        self.add_genre(genre)
        self.add_artist(artist)


    def add_song(self, song):
        self.__class__.songs.append(song)
        self.__class__.count = self.__class__.count + 1
    
    def add_genre(self, genre):
        self.__class__.genres.append(genre)
        self.__class__.genre_count[genre] = self.__class__.genre_count[genre] + 1 if self.__class__.genre_count.get(genre) else 1
    
    def add_artist(self, artist):
        self.__class__.artists.append(artist)
        self.__class__.artist_count[artist] = self.__class__.artist_count[artist] + 1 if self.__class__.artist_count.get(artist) else 1
