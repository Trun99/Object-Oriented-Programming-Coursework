import tkinter as tk
import font_manager as fonts
import webbrowser

from check_track import CheckTracks
from create_track_lists import CreateTracks
from update_track import UpdateTracks

def check_track_clicked():
    status_lbl.configure(text="Check Track button was clicked!")
    CheckTracks(tk.Toplevel(window))
def create_track_lists3_clicked():
    status_lbl.configure(text="Create Track button was clicked!")
    CreateTracks(tk.Toplevel(window))
def update_track3_clicked():
    status_lbl.configure(text="Update Track button was clicked")
    UpdateTracks(tk.Toplevel(window))
    



window = tk.Tk()
window.geometry("520x180")
window.title("Track Player")

fonts.configure()

header_lbl = tk.Label(window, text="Click one of the buttons below to choose an option:")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

check_track_btn = tk.Button(window, text="Check Track", command=check_track_clicked)
check_track_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window, text="Create Track List", command=create_track_lists3_clicked)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_track_btn = tk.Button(window, text="Update Track", command=update_track3_clicked)
update_track_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 20))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
