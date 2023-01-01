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
        
        self.__class__.songs.append(name)
        self.__class__.genres.append(genre)
        self.__class__.artists.append(artist)

        self.__class__.artist_count[artist] = self.__class__.artist_count[artist] + 1 if self.__class__.artist_count.get(artist) else 1
        self.__class__.genre_count[genre] = self.__class__.genre_count[genre] + 1 if self.__class__.genre_count.get(genre) else 1
        self.__class__.count = self.__class__.count + 1
    
    # @classmethod
    # def artist_count(cl):
    #     return {artist for artist in cl.artists }
    
    # @classmethod 
    # def genre_count(cl):
    #     return cl.genres

# Song("Sara Smile", "Hall and Oates", "Pop")
# import ipdb; ipdb.set_trace()
