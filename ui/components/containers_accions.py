"""Connect the actions of the frames with the application logic services"""
import tkinter as tk
from classes.services_manager import ServicesManager

class Containers_Acctions:
    """Contains the logic interactions between the frames and the services"""
    def __init__(self):
        self. service_manager = ServicesManager ()

    def item_buttons_generation(self, frame_master):

        for service in self.service_manager.services_offered:
            button = tk.Button(frame_master, text=service.name)
            button.pack(side="top", padx= 10, pady=5, anchor="nw")
