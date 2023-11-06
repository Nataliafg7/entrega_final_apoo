import tkinter as tk
from tkcalendar import Calendar
import json
from tkinter import messagebox

class ReservaMesaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reserva de Mesa")
        
        # Cargar las reservas existentes desde el archivo JSON
        self.reservas = self.cargar_reservas()

        # Crear un Frame para organizar los widgets
        frame = tk.Frame(root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Etiqueta y entrada para el nombre del cliente
        tk.Label(frame, text="Nombre del Cliente:").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(frame)
        self.nombre_entry.grid(row=0, column=1)

        # Etiqueta y lista de selección para la hora
        tk.Label(frame, text="Hora de la Reserva:").grid(row=1, column=0)
        self.horas_disponibles = ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00"]
        self.hora_var = tk.StringVar()
        self.hora_var.set(self.horas_disponibles[0])  # Establecer la primera hora como predeterminada
        self.hora_menu = tk.OptionMenu(frame, self.hora_var, *self.horas_disponibles)
        self.hora_menu.grid(row=1, column=1)

        # Etiqueta y calendario para la fecha de reserva
        tk.Label(frame, text="Fecha de la Reserva:").grid(row=2, column=0)
        self.calendario = Calendar(frame, date_pattern="dd/mm/yyyy")
        self.calendario.grid(row=2, column=1)

        # Etiqueta y menú desplegable para seleccionar la mesa
        tk.Label(frame, text="Mesa:").grid(row=3, column=0)
        self.mesa_var = tk.StringVar()
        self.mesa_menu = tk.OptionMenu(frame, self.mesa_var, "Mesa 1", "Mesa 2", "Mesa 3", "Mesa 4","Mesa 5", "Mesa 6", "Mesa 7", "Mesa 8","Mesa 9", "Mesa 10", "Mesa 11", "Mesa 12","Mesa 13", "Mesa 14", "Mesa 15", "Mesa 16", "Mesa 17", "Mesa 18", "Mesa 19", "Mesa 20")
        self.mesa_menu.grid(row=3, column=1)

        # Botón para realizar la reserva
        tk.Button(frame, text="Reservar", command=self.realizar_reserva).grid(row=4, columnspan=2, pady=10)

    def cargar_reservas(self):
        try:
            with open("reservas.json", "r") as file:
                reservas = json.load(file)
        except FileNotFoundError:
            reservas = {}
        return reservas

    def realizar_reserva(self):
        nombre = self.nombre_entry.get()
        hora = self.hora_var.get()
        fecha = self.calendario.get_date()
        mesa = self.mesa_var.get()

        if not nombre or not hora or not fecha or not mesa:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Crear una clave única para la reserva
        reserva_id = f"{nombre}_{fecha}"

        if reserva_id in self.reservas:
            messagebox.showinfo("Reserva Existente", "Esta mesa ya está reservada para la fecha seleccionada.")
        else:
            # Agregar la nueva reserva al diccionario de reservas
            self.reservas[reserva_id] = {
                "nombre": nombre,
                "hora": hora,
                "fecha": fecha,
                "mesa": mesa
            }

            # Guardar las reservas en el archivo JSON
            with open("reservas.json", "w") as file:
                json.dump(self.reservas, file)

            messagebox.showinfo("Reserva Exitosa", f"La mesa {mesa} ha sido reservada con éxito para el {fecha} a las {hora}.")

def ejecutar_reserva_app():
    root = tk.Tk()
    app = ReservaMesaApp(root)
    root.mainloop()

if __name__ == "__main__":
    ejecutar_reserva_app()
