class LibraryItem:
    def __init__(self, name, director, link, rating=0 ):
        self.name = name
        self.director = director
        self.rating = rating
        self.link = link
        self.play_count = 0

    def info(self):
        return f"{self.name} - {self.director} - {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "🌟"
        return stars
    
