"""Paned container"""
import tkinter as tk
from ui.components.custom_frames import CustomFrames

class CustomPaned():
    """Keeps the custom paneds"""
    def __init__(self):
        self.custom_frames = CustomFrames()

    def home_paned(self, master):
        """Home paned to make the sells"""
        main_padend = tk.PanedWindow(master, relief="ridge", orient=tk.HORIZONTAL)
        main_padend.pack(fill="both", expand=True)

        rigth_padend = tk.PanedWindow(master, relief="ridge", orient=tk.VERTICAL)
        rigth_padend.pack(fill="y", expand=True)

        item_frame = self.custom_frames.item_buttons_frame(main_padend)

        total_frame = self.custom_frames.total_frame(rigth_padend)
        breakdown_frame = self.custom_frames.breakdown_frame(rigth_padend)

        rigth_padend.add(total_frame, minsize=100, width= 180)
        rigth_padend.add(breakdown_frame, minsize=200, width= 500)

        main_padend.add(item_frame, minsize=200, width=980)
        main_padend.add(rigth_padend, minsize = 200, width = 300)

        return main_padend

    def graphs_paned(self, master):
        """Graph paned to check the records"""
        body_frame = tk.PanedWindow(master, relief="ridge")
        body_frame.pack(side="bottom", fill="both", expand=True)

        return body_frame
