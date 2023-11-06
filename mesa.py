import tkinter as tk
from tkinter import ttk
import random
from tkinter import PhotoImage


class TablaMesas:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla de Mesas")
        self.titulos_mesas = [f"Mesa {i}" for i in range(1, 21)]
        self.estados_mesas = [random.choice(["Ocupada", "Disponible"]) for _ in range(20)]
        image = PhotoImage(file="disponibilidad.gif")
        image = image.subsample(3)

        # Crear una etiqueta (Label) para mostrar la imagen en la parte superior de la ventana
        image_label = tk.Label(root, image=image)
        image_label.image = image  # Guardar una referencia para evitar que la imagen sea eliminada
        image_label.pack()

        # Crear un árbol (Treeview) para mostrar la tabla
        self.tabla_mesas = ttk.Treeview(root, columns=("Mesa", "Estado"), show="headings")
        self.tabla_mesas.heading("Mesa", text="Mesa")
        self.tabla_mesas.heading("Estado", text="Estado")
        self.tabla_mesas.pack(padx=10, pady=10)

        # Agregar una barra de desplazamiento vertical
        yscrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tabla_mesas.yview)
        yscrollbar.pack(side="right", fill="y")
        self.tabla_mesas.configure(yscrollcommand=yscrollbar.set)

        # Configurar etiquetas para colores
        self.tabla_mesas.tag_configure('rojo', background='red', foreground='white')
        self.tabla_mesas.tag_configure('verde', background='green')

        # Inicializar la tabla con los títulos y estados aleatorios
        self.inicializar_tabla()

        # Agregar un botón de cerrar
        self.boton_cerrar = tk.Button(root, text="Cerrar", command=self.cerrar_ventana)
        self.boton_cerrar.pack(pady=10)

    def inicializar_tabla(self):
        for i in range(20):
            mesa = self.titulos_mesas[i]
            estado = self.estados_mesas[i]
            if estado == "Ocupada":
                self.tabla_mesas.insert("", "end", values=(mesa, estado), tags=('rojo',))
            else:
                self.tabla_mesas.insert("", "end", values=(mesa, estado), tags=('verde',))

    def cerrar_ventana(self):
        self.root.destroy()  # Cerrar la ventana actual
        if len(self.root.winfo_children()) == 0:
            # Si no quedan más ventanas, finalizar la aplicación
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TablaMesas(root)
    root.mainloop()
