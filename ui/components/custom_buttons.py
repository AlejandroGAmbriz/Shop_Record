"""Contains the custom buttopns"""
import tkinter as tk

class CustomButtons:
    """Container the custom buttons"""
    def __init__(self):
        self.home_image = tk.PhotoImage(file="assets/icon_home.png")
        self.graphs_image = tk.PhotoImage(file="assets/icon_graphs.png")

    def viwer_controler_button(self, frame_master):
        """Button to change between the views"""
        button = tk.Button(frame_master, image=self.home_image)
        button.pack(side="right", padx=10, pady=10)

