import tkinter as tk
from tkinter import messagebox

class ConsultarCuentasApp:
    def __init__(self, root, cuentas_mesas):
        self.root = root
        self.root.title("Consultar Cuentas")
        self.cuentas_mesas = cuentas_mesas

        # Crear una ventana principal para la funcionalidad de consultar cuentas
        self.ventana_consultar_cuentas = tk.Toplevel(root)
        self.ventana_consultar_cuentas.title("Consultar Cuentas")

        # Crear una etiqueta para seleccionar la mesa
        self.label_mesa = tk.Label(self.ventana_consultar_cuentas, text="Selecciona una mesa:")
        self.label_mesa.pack()

        # Crear un menú desplegable para seleccionar la mesa
        opciones_mesas = ["Mesa {}".format(i) for i in range(1, 21)]
        self.numero_mesa = tk.StringVar()
        self.menu_mesa = tk.OptionMenu(self.ventana_consultar_cuentas, self.numero_mesa, *opciones_mesas)
        self.menu_mesa.pack()

        # Crear un botón para consultar la cuenta
        self.boton_consultar = tk.Button(self.ventana_consultar_cuentas, text="Consultar Cuenta", command=self.mostrar_factura_consulta)
        self.boton_consultar.pack()

    def mostrar_factura_consulta(self):
        mesa_seleccionada = self.numero_mesa.get()
        if not mesa_seleccionada:
            return

        mesa_numero = int(mesa_seleccionada.split()[-1])  # Obtener el número de mesa
        if mesa_numero < 1 or mesa_numero > 20:
            return

        total_cuenta = self.cuentas_mesas[mesa_numero - 1]

        mensaje = f"Factura de la Mesa {mesa_numero}:\nTotal: ${total_cuenta:.2f}"
        messagebox.showinfo("Factura", mensaje)

    def ejecutar_consultar_cuentas(self):
        self.ventana_consultar_cuentas.mainloop()
