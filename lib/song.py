# import ipdb

class Song:
    count = 0
    genre = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        #sets song name
        self.name = name
        #sets artist name
        self.artist = artist
        #sets genre
        self.genre = genre
        #sets count to genres duplicates
        self.add_to_genre_count()
        #sets count to artist duplicates
        self.add_to_artist_count()
        #increments count per instences that are created
        Song.count += 1
        #appends genre to genre list
        Song.genres = self.add_to_genres(genre)
        #appends artists to artist list
        Song.artist = self.add_to_artist(artist)
        
    

    #if the instence attribute genre that is created is not 
    #in the class genre list, then it will add it to the list
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genre:
            cls.genre.append(genre)
        return cls.genre

    #if the instence attribute artist that is created is not 
    #in the class artist list, then it will add it to the list
    @classmethod
    def add_to_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        return cls.artists

    # for every genre that is dupicated in the dictionary,
    #it will increment the count by one to that genre in the dictionary
    def add_to_genre_count(self):
        if self.genre not in Song.genre_count:
            Song.genre_count[self.genre] = 1
        else:
            Song.genre_count[self.genre] += 1

    # for every artis that is dupicated in the dictionary,
    #it will increment the count by one to that artist in the dictionary
    def add_to_artist_count(self):
        if self.artist not in Song.artist_count:
            Song.artist_count[self.artist] = 1
        else:
            Song.artist_count[self.artist] += 1

song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")

# ipdb.set_trace()


