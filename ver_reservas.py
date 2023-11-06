import tkinter as tk
from tkinter import Text, Scrollbar
import json

def mostrar_reservas():
    # Crear una ventana emergente para mostrar las reservas
    ventana_reservas = tk.Toplevel()
    ventana_reservas.title("Reservas")

    # Leer las reservas desde el archivo JSON
    try:
        with open("reservas.json", "r") as file:
            reservas = json.load(file)
    except FileNotFoundError:
        reservas = {}

    # Crear un widget Text para mostrar las reservas
    reservas_text = Text(ventana_reservas, wrap=tk.WORD, width=40, height=20)
    reservas_text.pack(fill=tk.BOTH, expand=True)

    # Agregar las reservas al widget Text
    for reserva_id, reserva_info in reservas.items():
        reserva_text = f"Nombre: {reserva_info['nombre']}\n"
        reserva_text += f"Hora: {reserva_info['hora']}\n"
        reserva_text += f"Fecha: {reserva_info['fecha']}\n"
        reserva_text += f"Mesa: {reserva_info['mesa']}\n\n"
        reservas_text.insert(tk.END, reserva_text)

    # Agregar una barra de desplazamiento para el widget Text
    scrollbar = Scrollbar(ventana_reservas, command=reservas_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    reservas_text.config(yscrollcommand=scrollbar.set)

    # Deshabilitar la edición en el widget Text
    reservas_text.config(state=tk.DISABLED)
