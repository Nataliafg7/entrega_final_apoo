import tkinter as tk
from informe_mesero  import ejecutar_informe_app
from informe_mesa import ejecutar_informe_mesa_app  # Importar la función del informe de mesa

class MenuVentas:
    def __init__(self, root):
        self.root = root
        self.menu_ventas_frame = None


    def mostrar(self):
        if self.menu_ventas_frame is None:
            self.menu_ventas_frame = tk.Frame(self.root)
            self.menu_ventas_frame.pack()
            
            button_informe_mesero = tk.Button(self.menu_ventas_frame, text="Informe de Mesero que más Vendió", command=ejecutar_informe_app)
            button_informe_mesero.pack()
            button_informe_mesa = tk.Button(self.menu_ventas_frame, text="Informe de Mesa que más Consumió", command=ejecutar_informe_mesa_app)
            button_informe_mesa.pack()


    def ocultar(self):
        if self.menu_ventas_frame:
            self.menu_ventas_frame.pack_forget()
