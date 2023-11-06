import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class TablaMesas:
    def __init__(self, root):
        self.root = root

        self.root.title("Tabla de Mesas")
        self.titulos_mesas = [f"Mesa {i}" for i in range(1, 21)]
        self.estados_mesas = [random.choice(["Ocupada", "Disponible"]) for _ in range(20)]

        # Crear una imagen para el encabezado
        imagen_encabezado = Image.open("disponibilidad.gif")  
        imagen_encabezado = imagen_encabezado.resize((300, 200)) 
        imagen_encabezado_tk = ImageTk.PhotoImage(imagen_encabezado)

        # Crear un Label para mostrar la imagen del encabezado
        self.encabezado_label = tk.Label(root, image=imagen_encabezado_tk)
        self.encabezado_label.image = imagen_encabezado_tk
        self.encabezado_label.pack(padx=10, pady=10)

        self.tabla_mesas = ttk.Treeview(root, columns=("Mesa", "Estado"), show="headings")
        self.tabla_mesas.heading("Mesa", text="Mesa")
        self.tabla_mesas.heading("Estado", text="Estado")
        self.tabla_mesas.pack(padx=10, pady=10)

        self.tabla_mesas.tag_configure('rojo', background='red', foreground='white')
        self.tabla_mesas.tag_configure('verde', background='green', foreground='white')

        self.inicializar_tabla()

        # Agregar un botón "Cerrar" para cerrar la ventana
        button_cerrar = tk.Button(root, text="Cerrar", command=self.cerrar_ventana)
        button_cerrar.pack()

    def inicializar_tabla(self):
        for i in range(20):
            mesa = self.titulos_mesas[i]
            estado = self.estados_mesas[i]
            etiqueta_color = 'rojo' if estado == "Ocupada" else 'verde'
            self.tabla_mesas.insert("", "end", values=(mesa, estado), tags=(etiqueta_color,))

    def mostrar_disponibilidad(self):
        ventana_tabla = tk.Toplevel()
        app = TablaMesas(ventana_tabla)

    def cerrar_ventana(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TablaMesas(root)
    root.mainloop()
