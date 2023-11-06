import tkinter as tk
from tkinter import Button, Label, Toplevel, Frame
import json

class Mesero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventas_por_mes = {}

    def registrar_venta(self, mes, monto):
        if mes in self.ventas_por_mes:
            self.ventas_por_mes[mes] += monto
        else:
            self.ventas_por_mes[mes] = monto

    def total_ventas(self):
        return sum(self.ventas_por_mes.values())

class InformeVentas:
    def __init__(self, root):
        self.root = root
        self.root.title("Informe de Ventas")
        self.meseros = []

        # Crear algunos meseros con ventas ficticias
        mesero1 = Mesero("Natalia")
        mesero1.registrar_venta("Enero", 1500.0)
        mesero1.registrar_venta("Febrero", 1200.0)

        mesero2 = Mesero("Juli")
        mesero2.registrar_venta("Enero", 1800.0)
        mesero2.registrar_venta("Febrero", 1300.0)

        mesero3 = Mesero("Angie")
        mesero3.registrar_venta("Enero", 1600.0)
        mesero3.registrar_venta("Febrero", 1000.0)

        self.meseros.extend([mesero1, mesero2, mesero3])

        # Crear botón para generar el informe
        btn_generar_informe = Button(root, text="Generar Informe", command=self.generar_informe)
        btn_generar_informe.pack(padx=10, pady=10)

    def generar_informe(self):
        # Crear una ventana emergente para mostrar el informe
        ventana_informe = Toplevel()
        ventana_informe.title("Informe de Ventas")

        informe_text = "Informe de Ventas:\n\n"

        mesero_mas_vendedor = max(self.meseros, key=lambda mesero: mesero.total_ventas())

        for mesero in self.meseros:
            informe_text += f"Mesero: {mesero.nombre}\n"
            for mes, ventas in mesero.ventas_por_mes.items():
                informe_text += f"  Mes {mes}: ${ventas:.2f}\n"
            informe_text += f"  Total de Ventas: ${mesero.total_ventas():.2f}\n"
            if mesero == mesero_mas_vendedor:
                informe_text += "  (Más Vendió)\n"
            informe_text += "\n"

        label_informe = Label(ventana_informe, text=informe_text)
        label_informe.pack(padx=10, pady=10)

def ejecutar_informe_app():
    root = tk.Tk()
    app = InformeVentas(root)
    root.mainloop()

if __name__ == "__main__":
    ejecutar_informe_app()
