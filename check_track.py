import tkinter as tk # Importing tkinter for GUI elements
import tkinter.scrolledtext as tkst # Importing scrolled text widget for scrollable text areas

# Importing necessary modules
import track_library as lib
import font_manager as fonts
from track_library import TrackLibrary
import check_track as CheckTracks
from PIL import Image, ImageTk # For handling images in the GUI


# Function to set text in a text area (used for displaying content)
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clears any existing text in the area
    text_area.insert(1.0, content)   # Inserts the new content at the beginning
import csv # Importing CSV module for CSV file handling
from library_item import LibraryItem  # Importing LibraryItem class for handling individual library items

# Function to list all tracks in the library
def list_all(self):
       # Display the entire song list
        output = ""  # Initialize an empty string to hold the output
        for key in self.library:  # Loop through the library dictionary
            item = self.library[key]  # Retrieve the item (track) by its key
            output += f"{key} {item.info()}\n" # Append the track's info to the output string
        return output # Return the full output of track details

def list_track(self, playlist): # Function to list tracks by playlist 
        # Display the song list based on the playlist
        output = "" # Initialize an empty string for the output
        for index, key in enumerate(playlist): # Enumerate through the playlist (giving an index to each track)
            item = self.library[key]   # Retrieve the track by its key from the library
            output += f"{index + 1} //: {key} {item.info()} - Playcount: {item.play_count}\n"  # Append track info and play count
        return output # Return the full list of tracks

# Function to get the name of a track by its key
def get_name(self, key):
      # Get the name of the song based on its key
        try:
            item = self.library[key] # Try to get the track by its key
            return item.name # Return the name of the track
        except KeyError: # If track is not found by the key
            return None  # Return None if track does not exist
# Function to get the director or artist of a track
def get_director(self, key):
       # Get the director or artist based on the track's key
        try:
            item = self.library[key] # Try to retrieve the track
            return item.director # Return the director/artist of the track
        except KeyError:  # If the track is not found by the key
            return None # Return None if track does not exist

# Function to get the rating of a track
def get_rating(self, key):
         # Get the play count or rating of the track
        try:
            item = self.library[key]  # Try to retrieve the track
            return item.rating  # Return the rating of the track
        except KeyError:  # If track does not exist in the library
            return -1  # Return -1 as a default value for non-existing tracks

# Function to set or update the rating for a track
def set_rating(self, key, rating):
        # Update the rating for the track
        try:
            item = self.library[key] # Try to get the track from the library
            item.set_rating(rating)# Set the rating of the track
            self.save_to_csv()  # Save changes to the CSV file
        except KeyError: # If track with the key doesn't exist
            print(f"Track and number '{key}' is not exist.")  # Print an error message

# Function to increment the play count of a track
def increment_play_count(self, key):
        # Increase the play count of the track
        try:
            item = self.library[key] # Try to retrieve the track by its key
            item.play_count += 1 # Increment the play count by 1
            self.save_to_csv()  # Save changes to the CSV file
        except KeyError:# If track is not found
            print(f"Track and number '{key}' is not exist.") # Print an error message

# Function to search for a track or artist by name
def search(self, search_term):
        # Search for songs or artists by name
        search_term = search_term.lower()   # Convert search term to lowercase for case-insensitive search
        results = [] # Initialize an empty list to hold search results
        for key, item in self.library.items():# Loop through all items in the library
            # Check if the search term matches the track name or director/artist name
            if search_term in item.name.lower() or search_term in item.director.lower():  # Kiểm tra nếu tên bài hát hoặc nghệ sĩ chứa chuỗi tìm kiếm
                results.append((key, item))  # Append matching results to the results list
        
        if results:# If there are results
            output = "Results:\n"  # Initialize output with the search header
            for key, item in results: # Loop through the results
                output += f"{key} {item.info()}\n" # Append each result to the output string
        else:
            output = "No reasults found.\n"  # No results found
        
        return output # Return the search results


# Class to manage the track check functionality in the GUI


class CheckTracks():
    def __init__(self, window):
        window.geometry("750x350") # Set the window size
        window.title("Check Track") # Set the window title

        # Create a button to list all tracks
        list_track_btn = tk.Button(window, text="List All Track", command=self.list_track_clicked)
        list_track_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create a label for entering a track number
        enter_lbl = tk.Label(window, text="Enter Number:")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Create a text entry for the user to input track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create a button to view a specific track
        check_track_btn = tk.Button(window, text="View Track", command=self.check_track_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create a scrolled text widget to display the list of tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create a text widget to display track details
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Create a label for displaying an image
        self.image_label = tk.Label(window) 
        self.image_label.grid(row=1,column=4, sticky="NW",padx=10, pady=10)

        # Create a label for status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Automatically list all tracks when the application starts
        self.list_track_clicked()

    def check_track_clicked(self):
        # Get the user input
        key = self.input_txt.get()
         # Fetch the track details using TrackLibrary
        name = TrackLibrary().get_name(key)
        if name is not None:
            # If the track exists, fetch and display its details
            director = TrackLibrary().get_director(key) 
            rating = TrackLibrary().get_rating(key)
            play_count = TrackLibrary().get_play_count(key)
            track_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
            self.load_image(key) # Load and display the corresponding image
        else:
            # If the track does not exist, display a not found message
            set_text(self.track_txt, f"Track {key} not found")
            self.image.label_config(image="")
            # Update the status label
        self.status_lbl.configure(text="Check Track button was clicked!")

    def list_track_clicked(self):
        # Fetch and display the list of all tracks
        track_list = TrackLibrary().list_all()
        set_text(self.list_txt, track_list)
        # Update the status label
        self.status_lbl.configure(text="List Track button was clicked!")

    def load_image(self, key):
        try:
         # Attempt to load and display the image for the given track key
            img_path = f"Image/{key}.jpg"  
            img = Image.open(img_path)
            img = img.resize((150, 150)) # Resize the image to fit the label
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img  
        except FileNotFoundError:
            # If no image is found, clear the image label and update the status
            self.image_label.config(image="")
            self.status_lbl.configure(text=f"No image found for Track {key}")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckTracks(window)     # open the CheckTracks GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
