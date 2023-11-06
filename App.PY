import tkinter as tk
from mesero import Mesero  
from menu_mesas import MenuMesas  # Importa la clase MenuMesas desde menu_mesas.py
from menu_ventas import MenuVentas  # Importa la clase MenuVentas desde menu_ventas.py



if __name__ == "__main__":
    root = tk.Tk()
    app = Mesero(root)
    root.mainloop()
