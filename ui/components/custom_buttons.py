"""Contains the custom buttopns"""
import tkinter as tk
class CustomButtons:
    """Container the custom buttons"""
    def __init__(self):
        self.home_image = tk.PhotoImage(file="assets/icon_home.png")
        self.graphs_image = tk.PhotoImage(file="assets/icon_graphs.png")
        self.add_image = tk.PhotoImage(file="assets/icon_add.png")
        self.remove_image = tk.PhotoImage(file="assets/icon_remove.png")
        self.mod_image = tk.PhotoImage(file="assets/icon_mod.png")

    def viwer_controler_button(self, frame_master):
        """Button to change between the views"""
        button = tk.Button(frame_master, image = self.home_image)
        button.pack(side="right", padx=10, pady=10 )

    def add_item_button(self, frame_master):
        """Button to add a new item to the seller list"""
        button = tk.Button(frame_master, image = self.add_image)
        button.pack(side="right", padx=5, pady=10, anchor="n")

    def remove_item_button(self, frame_master):
        """Button to remove a item of the seller list"""
        button = tk.Button(frame_master, image = self.remove_image)
        button.pack(side="right", padx=5, pady=10, anchor="n")

    def mod_item_button(self, frame_master):
        """Button to mod an item of the seller list"""
        button = tk.Button(frame_master, image = self.mod_image)
        button.pack(side="right", padx=5, pady=10, anchor="n")
