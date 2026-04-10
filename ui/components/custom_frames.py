"""Contains the custom frames"""
import tkinter as tk
from ui.constants import BUSSINES_NAME
from ui.components.custom_buttons import CustomButtons
from ui.components.containers_accions import Containers_Acctions

class CustomFrames():
    """Containe of the custom frames"""
    def __init__(self):
        self.custom_buttons = CustomButtons()
        self.containters_acctions = Containers_Acctions()

    def title_name_frame(self, master):
        """This fame have to be on the top of the view """
        top_frame = tk.Frame(master, relief="ridge")
        top_frame.pack(side="top", fill="x", expand= True)

        label_try = tk.Label(top_frame, text=BUSSINES_NAME)
        label_try.pack(side="left", expand=True, pady=10)

        self.custom_buttons.viwer_controler_button(top_frame)

        return top_frame

    def item_buttons_frame(self, master):
        """Frame for the item buttons for sell"""
        body_frame = tk.Frame(master, background="pink", relief="ridge")

        self.custom_buttons.add_item_button(body_frame)
        self.custom_buttons.remove_item_button(body_frame)
        self.custom_buttons.mod_item_button(body_frame)

        self.containters_acctions.item_buttons_generation(body_frame)

        return body_frame

    def total_frame(self, master):
        """Frame of the Total of the sell"""
        frame_total = tk.Frame(master, background="red")
        total_label = tk.Label(frame_total, text="Total:")
        total_label.pack(pady= 10)

        return frame_total

    def breakdown_frame(self, master):
        """Frame for the breakdown of the sell"""
        frame_breakdown = tk.Frame(master, background="grey")
        breakdown_label = tk.Label(frame_breakdown, text="Breakdown")
        breakdown_label.pack(pady= 10)

        return frame_breakdown
