"""Views for the iteraction for the items"""
import tkinter as tk

class ItemView:
    """Container of the views for the item interactions"""
    def __init__(self):
        pass

    def add_item_view(self):
        """View to add an item"""
        add_root = tk.Tk()

        add_root.geometry("400x200")

        label = tk.Label(add_root, text= "Ingrese los datos para el nuevo producto: ")
        label.pack(padx= 10, pady= 10)

        name_entry = tk.Entry(add_root, fg="grey", width= 30)
        name_entry.insert(0, "Incerte el nombre del producto: ")
        name_entry.pack(padx=10, pady=10)

        price_entry = tk.Entry(add_root, fg="grey", width= 30)
        price_entry.insert(0, "Incerte el precio del producto: ")
        price_entry.pack(padx=10, pady=10)

        button = tk.Button(add_root, text="Continuar")
        button.pack(padx= 10, pady=10)

        add_root.mainloop()

    def mod_item_view(self):
        """View to modify an item"""
        mod_root = tk.Tk()

        mod_root.geometry("400x200")

        label = tk.Label(mod_root, text= "Modifique la informacion de 'nombre_prodcuto'")
        label.pack(padx= 10, pady= 10)

        name_entry = tk.Entry(mod_root, fg="grey", width= 30)
        name_entry.insert(0, "nombre del producto ")
        name_entry.pack(padx=10, pady=10)

        price_entry = tk.Entry(mod_root, fg="grey", width= 30)
        price_entry.insert(0, "precio del producto ")
        price_entry.pack(padx=10, pady=10)

        button = tk.Button(mod_root, text="Continuar")
        button.pack(padx= 10, pady=10)

        mod_root.mainloop()


if __name__ == "__main__":
    item_view = ItemView()
    item_view.add_item_view()
    item_view.mod_item_view()
