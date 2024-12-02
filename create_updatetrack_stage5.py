import tkinter as tk # Import the tkinter library for creating GUI components
import tkinter.scrolledtext as tkst # Import tkinter's ScrolledText widget for scrollable text areas
import webbrowser # Import the webbrowser module to open links in the default browser
import track_library as lib # Import a custom library to manage the track library
import font_manager as fonts # Import a custom font manager for consistent font styles
from tkinter import messagebox # Import messagebox from tkinter to display pop-up alerts
from track_library import TrackLibrary # Import TrackLibrary class for handling track information and data
from library_item import LibraryItem # Import LibraryItem class to represent individual track details
from PIL import Image, ImageTk # Import the PIL library for image manipulation and display
import check_track as CheckTracks # Import a custom module for additional functionality related to track checking
import csv # Import the csv module for exporting playlist data to a CSV file

# Function to set the content of a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

# Playlist class to manage track list creation, updates, and display
class Playlist:
    def __init__(self, window):
        window.geometry("900x450")  # Set window size
        window.title("Create Track List")  # Window title
        self.track = []  # Initialize empty track list
        self.position = 0  # Initialize track position
        self.num = 0  # Initialize track counter
        self.tracklibrary = TrackLibrary()  # Create TrackLibrary instance

        # Define UI elements like buttons, labels, and text fields
        Play_btn = tk.Button(window, text="Play", activebackground="green yellow", command=self.play_track_clicked)
        Play_btn.grid(row=0, column=0, padx=10, pady=10) # Positioning Play button in grid

        enter_lbl = tk.Label(window, text="SpotiChill'🎧",font=("Helvetica", 18, "bold"))
        enter_lbl.grid(row=0, column=3, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Music For Life📀♬₊.🎧⋆☾⋆⁺₊🎸 🫧💗✨", font=("Helvetica", 18, "bold"))
        enter_lbl.grid(row=2, column=3, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # Positioning label for track number input

        enter_lbl = tk.Label(window, text="Enter Track Rating")
        enter_lbl.grid(row=3, column=3, padx=10, pady=10)# Positioning label for track rating input

        self.key_input_txt = tk.Entry(window, width=3)  # Text entry for track key input
        self.key_input_txt.grid(row=0, column=2, padx=10, pady=10)# Positioning input field for track number

        self.rating_input_txt = tk.Entry(window, width=3)  # Text entry for rating input
        self.rating_input_txt.grid(row=3, column=4, padx=10, pady=10) # Positioning input field for track rating

        add_btn = tk.Button(window, text="Add to Playlist", command=self.add_track_clicked, activebackground="green yellow")# Button to add track to playlist
        add_btn.grid(row=0, column=6, padx=10, pady=10)# Positioning "Add to Playlist" button

        self.list_txt = tkst.ScrolledText(window, width=20, height=10, wrap="none")  # Scrolled text area for the track list
        self.list_txt.grid(row=1, column=6, columnspan=3, sticky="NW", padx=10, pady=10)# Positioning track list display

        previous_btn = tk.Button(window, text="⏮", command=self.previous_track_clicked, activebackground="green yellow")# Button for navigating to the previous track
        previous_btn.grid(row=1, column=3, padx=10, pady=10, sticky="W") # Positioning "Previous Track" button

        enter_lbl = tk.Label(window, text="▶•၊၊||၊|။|||| ၊၊||၊|။|||| |||။|||| |။|||| |။|||| |။||||")
        enter_lbl.grid(row=1, column=3, padx=10, pady=10)

        check_track_btn = tk.Button(window, text="Check Track", command=self.check_track_clicked, activebackground="green yellow")# Button to check details of the current track
        check_track_btn.grid(row=0, column=3, padx=10, pady=10, sticky="W")# Positioning "Check Track" button

        next_track_btn = tk.Button(window, text="⏭", command=self.next_track_clicked, activebackground="green yellow")# Button for navigating to the next track
        next_track_btn.grid(row=1, column=3, padx=10, pady=10, sticky="E")# Positioning "Next Track" button

        update_btn = tk.Button(window, text="Update Track", command=self.update_track_clicked, activebackground="green yellow")# Button to update the track details
        update_btn.grid(row=3, column=0, padx=10, pady=10) # Positioning "Update Track" button

        self.libary_txt = tkst.ScrolledText(window, width=54, height=12, wrap="none")  # Scrolled text for library display
        self.libary_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Positioning track library display

        reset_btn = tk.Button(window, text="Reset Here!", command=self.reset_track_clicked, activebackground="green yellow")# Button to reset track input fields
        reset_btn.grid(row=3, column=1, padx=10, pady=10) # Positioning "Reset Here!" button

        self.track_txt = tk.Text(window, width=36, height=4, wrap="none")  # Text area for track details
        self.track_txt.grid(row=1, column=3, columnspan=3, sticky="NW", padx=10, pady=10)

        self.image_label = tk.Label(window)  # Label for displaying images
        self.image_label.grid(row=1, column=4, sticky="NW", padx=10, pady=90)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))  # Status label to show current action
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.input_searching_name = tk.Entry(window)  # Search input for track names
        self.input_searching_name.grid(row=2, column=6, padx=10, pady=10)

        search_btn = tk.Button(window, text="Search", command=self.searching_name)  # Search button to trigger track search
        search_btn.grid(row=2, column=7, padx=10, pady=10)

        self.list_all()  # Display all tracks in the library initially

    def searching_name(self):
        """Search for tracks by name in the library."""
        self.list_txt.delete(1.0, tk.END)  # Clear the text area
        search_name = self.input_searching_name.get().lower()  # Get the search term in lowercase
        result = [
            track for track in self.tracklibrary.list_all().split('\n')  # Use the TrackLibrary instance
            if search_name in track.lower()  # Perform case-insensitive search
        ]
        if result:
            set_text(self.list_txt, '\n'.join(result))  # Display matching tracks
        else:
            set_text(self.list_txt, "No matching tracks found.")  # Show no results

    def save_to_csv(self):
        """Save the current playlist to a CSV file."""
         
         # Check if the playlist is empty, and show an error message if it is
        if not self.track: 
            messagebox.showerror("Error", "Playlist is empty. Add tracks before saving.")
            return

        file_path = "playlist.csv"  # File to save  # Define the file path where the CSV will be saved
        try:
             # Open the file in write mode ('w') with UTF-8 encoding to handle special characters
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)   # Create a CSV writer object
                writer.writerow(["Key", "Name", "Director", "Rating", "Play Count"])# Write the header row

                  # Iterate through each track in the playlist
                for key in self.track:
                    # Get the track item using the key from the track library
                    item = self.tracklibrary.library.get(key)
                     # If the item exists, write the track details to the CSV
                    if item:
                        writer.writerow([key, item.name, item.director, item.rating, item.play_count])

          # If an exception occurs during the file operation, show an error message
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save playlist: {str(e)}")

    def list_all(self):
        """Display all tracks in the library."""
        output = ""
        for key, item in self.tracklibrary.library.items():  # Adjust according to TrackLibrary's structure
            output += f"{key} {item.info()}\n"
        set_text(self.libary_txt, output)

    def on_listbox_select(self, event):
        """Handle listbox selection."""
        try:
            selected_index = self.listbox.curselection()[0]
            selected_text = self.listbox.get(selected_index)
            key = selected_text.split(":")[0].strip()  # Extract the track key
            self.key_input_txt.delete(0, tk.END)
            self.key_input_txt.insert(0, key)
            self.check_track_clicked()  # Display track details
        except IndexError:
            pass  # No selection

    def show_track(self):
        """Display the current track details."""
        key = self.track[self.position]
        name = self.tracklibrary.get_name(key)
        director = self.tracklibrary.get_director(key)
        rating = self.tracklibrary.get_rating(key)
        track_details = f"{name}\n{director}\nrating: {rating}"
        set_text(self.track_txt, track_details)

    def previous_track_clicked(self):
        """Handle the previous track button click."""
        self.status_lbl.configure(text="Previous Track button was clicked!")
        x = len(self.track)
        if x == 0:
            messagebox.showerror("Error", "NO TRACK IN THE PLAYLIST")
        elif self.position < x:
            try:
                self.position -= 1
                self.show_track()
            except:
                self.position += x
                self.show_track()
        elif self.position < 0:
            self.position = x
            self.show_track()

    def next_track_clicked(self):
        """Handle the next track button click."""
        self.status_lbl.configure(text="Next Track button was clicked!")
        x = len(self.track)
        if x == 0:
            messagebox.showerror("Error", "THERE ARE NO SONGS IN THE PLAYLIST!")
        elif self.position < x:
            try:
                self.position += 1
                self.show_track()
            except:
                self.position = 0
                self.show_track()
        else:
            self.position = 0
            self.show_track()

    def add_track(self):
        """Add track to playlist."""
        key = self.key_input_txt.get()
        self.track.append(key)
        output = self.tracklibrary.list_track(self.track)
        set_text(self.list_txt, output)

    def update_playlist_display(self):
        """Update the playlist display after modification."""
        output = self.tracklibrary.list_track(self.track)
        set_text(self.list_txt, output)

    def check_track_clicked(self):
        """Check and display the track details."""
        key = self.key_input_txt.get()
        name = self.tracklibrary.get_name(key)
        if name is not None:
            director = self.tracklibrary.get_director(key)
            rating = self.tracklibrary.get_rating(key)
            track_details = f"{name}\n{director}\nrating: {rating}"
            set_text(self.track_txt, track_details)
            self.load_image(key)
        else:
            set_text(self.track_txt, f"Track {key} not found")

        self.status_lbl.configure(text="Check Track button was clicked!")

    def play_all(self):
        """Play all tracks in the playlist."""
        if not self.track:
            messagebox.showerror("Error", "NO TRACKS IN THE PLAYLIST")
            return
        for key in self.track:
            self.tracklibrary.increment_play_count(key)

    def add_track_clicked(self):
        """Add track to playlist on button click."""
        key = self.key_input_txt.get()
        name = self.tracklibrary.get_name(key)
        if name is not None:
            self.add_track()
            self.num += 1
            if self.num == 1:
                director = self.tracklibrary.get_director(key)
                rating = self.tracklibrary.get_rating(key)
                track_details = f"{name}\n{director}\nrating: {rating}"
                set_text(self.track_txt, track_details)
        else:
            messagebox.showerror("Error", "Please enter a valid number!")
        self.status_lbl.configure(text="Add button was clicked!")

    def play_track_clicked(self):
        """Play a single track from the playlist."""
        key = self.key_input_txt.get()
        link = self.tracklibrary.get_link(key)
        if link:
            webbrowser.open(link)  # Open the link in the default browser
            self.tracklibrary.increment_play_count(key)  # Increment play count
            self.update_playlist_display()  # Update display
            self.status_lbl.configure(text=f"Playing {self.tracklibrary.get_name(key)}!")

            # Automatically save the playlist to CSV after playing
            self.save_to_csv()
            self.status_lbl.configure(text="Playlist automatically saved!")

    def reset_track_clicked(self):
        """Reset the track list."""
        self.track.clear()
        output = self.tracklibrary.list_track(self.track)
        set_text(self.list_txt, output)
        self.status_lbl.configure(text="Reset button was clicked!")

    def update_track_clicked(self):
        """Update the track rating."""
        key = self.key_input_txt.get()
        try:
            rating = int(self.rating_input_txt.get())
            if rating >= 0 and rating <= 5:
                self.tracklibrary.set_rating(key, rating)
                self.update_display()
            else:
                messagebox.showerror("Error", "Please enter 0-5 rating!")
        except:
            messagebox.showerror("Error", "Please enter 0-5 rating!")
        self.status_lbl.configure(text="Update Track button was clicked!")

    def update_display(self):
        """Update track display after rating change."""
        key = self.key_input_txt.get()
        name = self.tracklibrary.get_name(key)
        director = self.tracklibrary.get_director(key)
        rating = self.tracklibrary.get_rating(key)
        track_details = f"{name}\n{director}\nrating: {rating}"
        set_text(self.track_txt, track_details)

    def load_image(self, key):
        """Load and display the track's image."""
        try:
            img_path = f"Image/{key}.jpg"   # Construct the image file path using the track key (e.g., "Image/123.jpg")
            img = Image.open(img_path)  # Attempt to open the image file at the specified path
            img = img.resize((150, 150))  # Resize the image to 150x150 pixels for display
            img = ImageTk.PhotoImage(img)   # Convert the image to a format that can be displayed by tkinter
            self.image_label.config(image=img)   # Set the image in the image_label widget for display
            self.image_label.image = img # Keep a reference to the image to prevent it from being garbage collected
        except FileNotFoundError: 
            self.image_label.config(image="")  # If the image file is not found, clear the image from the label
            self.status_lbl.configure(text=f"No image found for Track {key}") # Display a status message indicating the image was not found

# Main entry point to run the GUI application
if __name__ == "__main__":
    window = tk.Tk()  # Initialize the main window
    fonts.configure()  # Configure fonts
    Playlist(window)  # Create Playlist instance
    window.mainloop()  # Start the tkinter event loop
