"""Config of the main Viwew"""

import tkinter as tk
from ui.constants import BUSSINES_NAME
from ui.components.custom_frames import CustomFrames
from ui.components.custom_paneds import CustomPaned

class MainView():

    def __init__(self):
        self.root = tk.Tk()
        self.custom_frames = CustomFrames()
        self.custom_padeds = CustomPaned()
        self._view_confi()

    def _view_confi(self):
        """view config"""
        self.root.title(BUSSINES_NAME)
        self.root.geometry("1280x620")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def view_loop(self):

        main_panded = tk.PanedWindow(self.root, orient=tk.VERTICAL)
        main_panded.pack(fill="both", expand=True)
        main_panded.add(self.custom_frames.title_name_frame(main_panded))
        main_panded.add(self.custom_padeds.home_paned(main_panded))

        self.root.mainloop()
