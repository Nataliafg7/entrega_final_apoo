# informe_mesa.py
import tkinter as tk
from tkinter import Button, Label, Toplevel, Frame
import json

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.total_consumido = 0

    def registrar_consumo(self, monto):
        self.total_consumido += monto

class InformeMesa:
    def __init__(self, root):
        self.root = root
        self.root.title("Informe de Mesa")
        self.mesas = []

        # Crear algunas mesas con consumos ficticios
        mesa1 = Mesa(1)
        mesa1.registrar_consumo(500.0)
        mesa1.registrar_consumo(300.0)

        mesa2 = Mesa(2)
        mesa2.registrar_consumo(600.0)
        mesa2.registrar_consumo(750.0)

        mesa3 = Mesa(3)
        mesa3.registrar_consumo(450.0)
        mesa3.registrar_consumo(100.0)

        mesa9 = Mesa(9)
        mesa9.registrar_consumo(40.0)
        
        self.mesas.extend([mesa1, mesa2, mesa3, mesa9])

        # Crear botón para generar el informe
        btn_generar_informe = Button(root, text="Generar Informe de Mesa", command=self.generar_informe)
        btn_generar_informe.pack(padx=10, pady=10)

    def generar_informe(self):
        # Crear una ventana emergente para mostrar el informe
        ventana_informe = Toplevel()
        ventana_informe.title("Informe de Mesa")

        informe_text = "Informe de Mesa:\n\n"

        mesa_que_mas_consumio = max(self.mesas, key=lambda mesa: mesa.total_consumido)

        for mesa in self.mesas:
            informe_text += f"Mesa #{mesa.numero}\n"
            informe_text += f"  Total Consumido: ${mesa.total_consumido:.2f}\n"
            if mesa == mesa_que_mas_consumio:
                informe_text += "  (Más Consumió)\n"
            informe_text += "\n"

        label_informe = Label(ventana_informe, text=informe_text)
        label_informe.pack(padx=10, pady=10)

def ejecutar_informe_mesa_app():
    root = tk.Tk()
    app = InformeMesa(root)
    root.mainloop()
