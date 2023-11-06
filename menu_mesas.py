import tkinter as tk
from disponibilidad import TablaMesas  # Importa la clase TablaMesas desde tabla_mesas.py
import tkinter as tk
from PIL import Image, ImageTk
import os
import json
from tkinter import messagebox
from tkcalendar import Calendar
from ver_reservas import mostrar_reservas  # Importa la función mostrar_reservas

from reserva import ReservaMesaApp


class MenuMesas:
    def __init__(self, root):
        self.root = root
        self.menu_mesas_frame = None
    def mostrar(self):
        if self.menu_mesas_frame is None:
            self.menu_mesas_frame = tk.Frame(self.root)
            self.menu_mesas_frame.pack()

            button_disponibilidad = tk.Button(self.menu_mesas_frame, text="Ver Disponibilidad de Mesas", command=self.mostrar_tabla_mesas)
            button_disponibilidad.pack()
    def mostrar_tabla_mesas(self):
        ventana_tabla = tk.Toplevel()  # Crea una nueva ventana (ventana secundaria)
        app = TablaMesas(ventana_tabla)  # Crea una instancia de la clase TablaMesas

    def mostrar(self):
        if self.menu_mesas_frame is None:
            self.menu_mesas_frame = tk.Frame(self.root)
            self.menu_mesas_frame.pack()
            
            button_disponibilidad = tk.Button(self.menu_mesas_frame, text="Ver Disponibilidad de Mesas", command=self.mostrar_tabla_mesas)
            button_disponibilidad.pack()            
            
            boton_abrir_mesa_app = tk.Button(self.menu_mesas_frame, text="Agregar pedido a la mesa", command=abrir_mesa_app)
            boton_abrir_mesa_app.pack()
            
            button_hacer_reserva = tk.Button(self.menu_mesas_frame, text="Hacer Reserva de Mesa", command=self.ejecutarreserva_reserva)
            button_hacer_reserva.pack()
            
            button_info_reserva = tk.Button(self.menu_mesas_frame, text="Información de Reserva de Mesa",command=mostrar_reservas)
            button_info_reserva.pack()

           
    def ejecutarreserva_reserva(self):
       ejecutarreserva_app()

    def ocultar(self):
        if self.menu_mesas_frame:
            self.menu_mesas_frame.pack_forget()
import tkinter as tk
from agregar_pedido import MesaApp
def ejecutarreserva_app():
    root = tk.Tk()
    app = ReservaMesaApp(root)
    root.mainloop()
def ejecutar_app():
    root_mesa = tk.Toplevel()
    app = MesaApp(root_mesa)
    root_mesa.mainloop()

def abrir_mesa_app():
    ejecutar_app()

def mostrar_menu_principal():
    root = tk.Tk()
    root.title("Menú Principal")

    # Crea un botón en el menú para abrir MesaApp
   

    root.mainloop()
def mostrar_factura(self):
        mesa_seleccionada = int(self.numero_mesa.get().split()[-1])  # Obtener el número de mesa
        cuentas = self.cargar_cuentas_desde_json()

        # Buscar la cuenta de la mesa seleccionada en el archivo JSON
        for cuenta in cuentas:
            if cuenta["mesa"] == mesa_seleccionada:
                total = cuenta["total"]
                mensaje = f"Factura de la Mesa {mesa_seleccionada}:\nTotal: ${total:.2f}"
                messagebox.showinfo("Factura", mensaje)
                return

        # Si no se encontró una cuenta para la mesa seleccionada
        messagebox.showerror("Error", f"No se encontró una cuenta para la Mesa {mesa_seleccionada}")
if __name__ == "__main__":
    mostrar_menu_principal()
