import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox

import font_manager as fonts
from track_library import TrackLibrary
import update_track as UpdateTracks
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateTracks:
    def __init__(self,window):
        window.geometry("600x300")  # Set the size of the window
        window.title("Update Track")  # Set the title of the window
        self.tracklibrary = TrackLibrary()  # Create an instance of the TrackLibrary to interact with track data

        # Label and input field for track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # Position the label on the window

        self.key_input_txt = tk.Entry(window, width=3)  # Input field for entering track number
        self.key_input_txt.grid(row=0, column=2, padx=10, pady=10)  # Position the input field

        # Label and input field for track rating
        enter_lbl = tk.Label(window, text="Enter Track Rating")
        enter_lbl.grid(row=1, column=1, padx=10, pady=10)  # Position the label for rating

        self.rating_input_txt = tk.Entry(window, width=3)  # Input field for entering track rating
        self.rating_input_txt.grid(row=1, column=2, padx=10, pady=10)  # Position the input field

        # Button to update the track's rating
        update_btn = tk.Button(window, text="UpdateTrack", command=self.update_track_clicked)
        update_btn.grid(row=0, column=4, padx=10, pady=10)  # Position the update button

        # Button to check the details of a track
        check_track_btn = tk.Button(window, text="Check Track", command=self.check_track_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)  # Position the check button

        # Text area to display the track details or any relevant messages
        self.list_txt = tkst.Text(window, width=35, height=8, wrap="none")
        self.list_txt.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)  # Position the text area

        # Status label to display status messages like success or error
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)  # Position the status labelky="W", padx=10, pady=10)

    def update_display(self):  
        key = self.key_input_txt.get() # Get the track number entered by the user
        name = self.tracklibrary.get_name(key) # Get the name of the track from the track library
        director = self.tracklibrary.get_director(key) # Get the director of the track
        rating = self.tracklibrary.get_rating(key) # Get the rating of the track
        track_details = f"{name}\n{director}\nrating: {rating}"# Prepare the track details in a formatted string
        set_text(self.list_txt, track_details) # Update the text area with the track details

    def update_track_clicked(self): 
        key = self.key_input_txt.get()# Get the track number entered by the user
        try:
            rating = int(self.rating_input_txt.get())# Attempt to convert the entered rating to an integer
            if rating >=0 and rating <=5:# Check if the rating is within the valid range (0 to 5)
                self.tracklibrary.set_rating(key, rating) # Set the new rating for the track
            else:
                messagebox.showerror("Error", "Please enter 0-5 rating")# Show an error if the rating is not within the valid range
        except:
            messagebox.showerror("Error", "Please enter 0-5 rating")# Show an error if the rating is not a valid integer
        self.update_display()  # Update the display with the new track details
        self.status_lbl.configure(text="Update Track button was clicked!") # Update the status label

    def check_track_clicked(self):
        key = self.key_input_txt.get() # Get the track number entered by the user
        name = TrackLibrary().get_name(key)# Get the name of the track from the track library
        if name is not None: # If the track exists
            director = self.tracklibrary.get_director(key)  # Get the director of the track
            rating = self.tracklibrary.get_rating(key) # Get the rating of the track
            track_details = f"{name}\n{director}\nrating: {rating}" # Prepare the track details
            set_text(self.list_txt, track_details) # Update the text area with the track details
        elif name is None: # If the track does not exist
            set_text(self.list_txt, "Please enter valid number")  # Display an error message
        else:
            set_text(self.list_txt, f"Track {key} not found")# Display a not found message
        self.status_lbl.configure(text="Check Track button was clicked!")# Update the status label

if __name__ == "__main__":  
    window = tk.Tk()          # Create the main Tkinter window
    fonts.configure()       # Apply the custom font configuration
    UpdateTracks(window)    # Create the UpdateTracks instance and pass the window
    window.mainloop()        # Start the Tkinter main loop to run the application