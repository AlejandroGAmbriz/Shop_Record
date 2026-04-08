"""Contains the custom frames"""
import tkinter as tk
from ui.constants import BUSSINES_NAME
from ui.components.custom_buttons import CustomButtons

class CustomFrames():
    """Containe of the custom frames"""
    def __init__(self):
        self.custom_buttons = CustomButtons()

    def title_name_frame(self, master):
        """This fame have to be on the top of the view """
        top_frame = tk.Frame(master, relief="ridge")
        top_frame.pack(side="top", fill="x", expand= True)

        label_try = tk.Label(top_frame, text=BUSSINES_NAME)
        label_try.pack(side="left", expand=True, pady=10)

        self.custom_buttons.viwer_controler_button(top_frame)

        return top_frame

    def item_buttons_frame(self, master):
        """Keeps the item buttons for sell"""
        body_frame = tk.Frame(master, background="pink", relief="ridge")
        body_frame.pack(side="left", fill="y")

        return body_frame

    def total_frame(self, master):
        """Total of the sell"""
        frame_total = tk.Frame(master, background="red")
        frame_total.pack(side="right", fill="y")

        return frame_total

    def breakdown_frame(self, master):
        pass
