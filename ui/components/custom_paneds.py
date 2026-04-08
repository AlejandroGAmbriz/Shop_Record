"""Paned container"""
import tkinter as tk
from ui.components.custom_frames import CustomFrames

class CustomPaned():
    """Keeps the custom paneds"""
    def __init__(self):
        self.custom_frames = CustomFrames()

    def home_paned(self, master):
        body_frame = tk.PanedWindow(master, relief="ridge", orient=tk.HORIZONTAL)
        body_frame.pack(fill="both", expand=True)

        item_frame = self.custom_frames.item_buttons_frame(body_frame)
        item_frame.config(width=300)

        total_frame = self.custom_frames.total_frame(body_frame)
        total_frame.config(width=5)

        body_frame.add(total_frame, minsize=50)
        body_frame.add(item_frame, minsize=200)


        return body_frame

    def graphs_paned(self, master):
        body_frame = tk.PanedWindow(master, relief="ridge")
        body_frame.pack(side="bottom", fill="both", expand=True)

        return body_frame
