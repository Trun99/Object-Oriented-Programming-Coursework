import tkinter as tk  # Import the tkinter library for GUI components
import tkinter.scrolledtext as tkst # Import tkinter's ScrolledText widget for scrollable text areas

from tkinter import messagebox # Import messagebox from tkinter to display pop-up alerts

import create_track_lists as CreateTracks # Import the custom module to manage track list creation
import track_library as lib  # Import the custom library to handle track data
import font_manager as fonts  # Import the custom font manager to ensure consistent font styles
from track_library import TrackLibrary  # Import TrackLibrary class to manage track information
from library_item import LibraryItem  # Import LibraryItem class to represent individual track details


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear all the text in the text area from line 1 to the end
    text_area.insert(1.0, content) # Insert the new content starting from the first line

class CreateTracks:
    def __init__(self,window):
        window.geometry("800x400")  # Set the window size 
        window.title("Create Track List")   # Set the window title
        self.track = [] # Initialize an empty list to store tracks
        self.position = 0  # Track the current position in the playlist
        self.tracklibrary = TrackLibrary() # Instantiate the TrackLibrary object

         # Play button to trigger playing the track
        Play_btn = tk.Button(window, text="Play", command=self.play_track_clicked) 
        Play_btn.grid(row=0, column=0, padx=10, pady=10) # Place the button in the grid

         # Label for entering track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # Position the label in the grid

         # Text entry for inputting the track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # Place input text box

         # Button to add the track to the playlist
        add_btn = tk.Button(window, text="Add to playlist", command=self.add_track_clicked)
        add_btn.grid(row=0, column=3, padx=10, pady=10)# Place the button in the grid

        # Scrolled text widget to display the playlist
        self.list_txt = tkst.ScrolledText(window, width=54, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Place text area in grid

         # Button to reset the playlist
        reset_btn = tk.Button(window, text="Reset playlist", command=self.reset_track_clicked)
        reset_btn.grid(row=2, column=3, padx=10, pady=10)  # Position the reset button

         # Status label to display messages to the user
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Position the label

    def show_track(self):
        key = self.track[self.position]  # Get the track key at the current position in the playlist
        name = self.tracklibrary.get_name(key)  # Retrieve the name of the track from the library
        director = self.tracklibrary.get_director(key)   # Retrieve the director of the track
        rating = self.tracklibrary.get_rating(key)  # Retrieve the rating of the track
        track_details = f"{name}\n{director}\nrating: {rating}" # Format the track details as a string
        set_text(self.track_txt, track_details)   # Set the formatted details in the text area

        
    def add_track(self):
        key = self.input_txt.get() # Get the track key from the input field
        self.track.append(key)  # Get the track key from the input field
        output = self.tracklibrary.list_track(self.track)   # Get the updated list of tracks in the playlist
        set_text(self.list_txt, output)  # Display the updated playlist in the list text area
    def update_playlist_display(self):
        output = self.tracklibrary.list_track(self.track) # Get the current list of tracks in the playlist
        set_text(self.list_txt, output)   # Display the updated playlist in the list text area


    def play_all(self):
        if len(self.track) == 0: # Check if the playlist is empty
            messagebox.showerror("Error","NO SONG IN THE PLAYLIST") # Show an error message if empty
            return
        
        for key in self.track: # Loop through all tracks in the playlist
            self.tracklibrary.increment_play_count(key)# Increment the play count for each track

    def add_track_clicked(self):
        key = self.input_txt.get() # Get the track key from the input field
        name = self.tracklibrary.get_name(key) # Check if the track exists by its name
        if name is not None: # If the track exists
            self.add_track() # Add the track to the playlist
        else:
            messagebox.showerror("Error", "Please enter a valid number")  # Show an error if the track is invalid
        self.status_lbl.configure(text = "Add button was clicked") # Update the status label


    def play_track_clicked(self):
        self.play_all()# Play all tracks in the playlist
        self.update_playlist_display() # Update the display of the playlist
        self.status_lbl.configure(text = "Play button was clicked") # Update the status label

    def reset_track_clicked(self):
        self.track.clear()# Clear all tracks from the playlist
        output = self.tracklibrary.list_track(self.track) # Get the updated (empty) list of tracks
        set_text(self.list_txt, output) # Display the empty playlist
        self.status_lbl.configure(text = "Reset button was clicked") # Update the status label




if __name__ == "__main__":  
    window = tk.Tk()      # Create a new tkinter window   
    fonts.configure()        # Configure fonts for the window
    CreateTracks(window)     # Create the CreateTracks instance to manage track list creation
    window.mainloop()        # Start the tkinter event loop to make the window responsive