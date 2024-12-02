from library_item import LibraryItem

class TrackLibrary:
    def __init__(self):
        self.library = {}
        self.library["01"] = LibraryItem("Baby", "Justin Bieber", "https://www.youtube.com/watch?v=kffacxfA7G4",4)
        self.library["02"] = LibraryItem("Not Like Us", "Kendrick Lamar","https://www.youtube.com/watch?v=H58vbez_m4E", 5)
        self.library["03"] = LibraryItem("One More Night", "Maroon 5","https://www.youtube.com/watch?v=fwK7ggA3-bU", 2)
        self.library["04"] = LibraryItem("You Are Not Alone", "Micheal Jackson","https://www.youtube.com/watch?v=pAyKJAtDNCw", 1)
        self.library["05"] = LibraryItem("Counting Stars", "OneRepublic","https://www.youtube.com/watch?v=hT_nvWreIhg", 3)
        self.library["06"] = LibraryItem("Take Me Home,Country Road", "John Denver","https://www.youtube.com/watch?v=1vrEljMfXYo", 3)
        self.library["07"] = LibraryItem("We Don't Talk Anymore", "Charlie Puth","https://www.youtube.com/watch?v=3AtDnEC4zak", 3)
        self.library["08"] = LibraryItem("I Do", "911","https://www.youtube.com/watch?v=pBTp2RWxq-s", 3)
        self.library["09"] = LibraryItem("7 Years", "Lukas Graham","https://www.youtube.com/watch?v=LHCob76kigA", 3)
        self.library["10"] = LibraryItem("I Love You 3000", "Stephanie Poetri","https://www.youtube.com/watch?v=cPkE0IbDVs4", 3)


    def list_all_tracks(self):
        """Return a string with all tracks in the library."""
        output = ""
        for key, item in self.library.items():
            output += f"{key}: {item.info()}\n"
        return output
    def list_all(self):
        output = ""
        for key in self.library:
            item = self.library[key]
            output += f"{key} {item.info()}\n"
        return output
    
    def list_track(self, playlist):
        output = ""
        for index, key in enumerate(playlist):
            item = self.library[key]
            output += f"{index + 1} //: {key} {item.info()} - Playcount:{item.play_count}\n"
        return output

    def get_name(self, key):
        try:
            item = self.library[key]
            return item.name
        except KeyError:
            return None


    def get_director(self, key):
        try:
            item = self.library[key]
            return item.director
        except KeyError:
            return None


    def get_rating(self, key):
        try:
            item = self.library[key]
            return item.rating
        except KeyError:
            return -1


    def set_rating(self, key, rating):
        try:
            item = self.library[key]
            item.rating = rating
        except KeyError:
            return

    def get_play_count(self, key):
        try:
            item = self.library[key]
            return item.play_count
        except KeyError:
            return -1
   
    def get_link(self, key):
        try:
            item = self.library[key]
            return item.link
        except KeyError:
            return 
    

    """def get_pc(self, key):
        try:
            item = self.library[key]
            return item.play_count
        except:
            return"""

    def increment_play_count(self, key):
        try:
            item = self.library[key]
            item.play_count += 1
        except KeyError:
            return

    def list_all_tracks(self):
        """Trả về danh sách toàn bộ bài hát dưới dạng chuỗi."""
        output = ""
        for key, item in self.library.items():
            output += f"{key}: {item.info()}\n"
        return output