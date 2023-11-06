import tkinter as tk
from PIL import Image, ImageTk
import os
import json

platos = [
    {"nombre": "Café expreso", "precio": 3.000, "imagen": "1.png"},
{"nombre": "Whisky", "precio": 40.000, "imagen": "2.png"},
{"nombre": "Té negro", "precio": 7.000, "imagen": "3.png"},
{"nombre": "Coctel rainbow paradise", "precio": 50.000, "imagen": "4.png"},
{"nombre": "Coca cola", "precio": 5.000, "imagen": "5.png"},
{"nombre": "Vino", "precio": 40.000, "imagen": "6.png"},
{"nombre": "Limonada con menta", "precio": 7.000, "imagen": "7.png"},
{"nombre": "Botella de agua", "precio": 3.000, "imagen": "8.png"},
{"nombre": "Jugos naturales", "precio": 10.000, "imagen": "9.png"},
{"nombre": "Sushi", "precio": 30.000, "imagen": "10.png"},
{"nombre": "Hamburguesa", "precio": 30.000, "imagen": "11.png"},
{"nombre": "Tacos", "precio": 30.000, "imagen": "12.png"},
{"nombre": "Ensalada", "precio": 25.000, "imagen": "13.png"},
{"nombre": "Sopa de verduras", "precio": 20.000, "imagen": "14.png"},
{"nombre": "Pescado", "precio": 30.000, "imagen": "15.png"},
{"nombre": "Pechuga de pollo", "precio": 30.000, "imagen": "16.png"},
{"nombre": "Pizza Margherita", "precio": 40.000, "imagen": "17.png"},
{"nombre": "Pasta", "precio": 20.000, "imagen": "18.png"},
{"nombre": "Copa de helado", "precio": 12.000, "imagen": "19.png"},
{"nombre": "Cerveza", "precio": 5.000, "imagen": "20.png"},
]

class MesaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Mesas")
        self.cuentas_mesas = [0] * 20
        self.pedidos = {}  # Diccionario para llevar un registro de los pedidos

        # Obtén la ruta absoluta del directorio donde se encuentra este script
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        # Cargar pedidos desde el archivo JSON
        self.cargar_pedidos()

        # Crear una imagen para el encabezado
        imagen_encabezado = Image.open("agregar_pedido.gif")
        imagen_encabezado = imagen_encabezado.resize((300, 200))
        imagen_encabezado_tk = ImageTk.PhotoImage(imagen_encabezado)

        # Crear un Label para mostrar la imagen del encabezado
        self.encabezado_label = tk.Label(root, image=imagen_encabezado_tk)
        self.encabezado_label.image = imagen_encabezado_tk
        self.encabezado_label.pack(padx=10, pady=10)

        # Crear un Frame para organizar los botones de las mesas en 4 columnas
        mesas_frame = tk.Frame(root)
        mesas_frame.pack()

        # Crear botones para las mesas en 4 columnas
        self.botones_mesas = []
        for i in range(20):
            boton_mesa = tk.Button(mesas_frame, text=f"Mesa {i + 1}", command=lambda i=i: self.mostrar_carta(i))
            boton_mesa.grid(row=i // 4, column=i % 4, padx=10, pady=10)
            self.botones_mesas.append(boton_mesa)

        # Botón para consultar cuentas
        boton_consultar_cuentas = tk.Button(root, text="Consultar Cuentas", command=self.consultar_cuentas)
        boton_consultar_cuentas.pack()

        # Agregar un botón "Cerrar" para cerrar la ventana
        button_cerrar = tk.Button(root, text="Cerrar", command=self.cerrar_ventana)
        button_cerrar.pack()

    def mostrar_carta(self, numero_mesa):
        ventana_carta = tk.Toplevel(self.root)
        ventana_carta.title(f"Carta de Mesa {numero_mesa + 1}")
        
        
        # Crear un Canvas para la ventana de la carta
        carta_canvas = tk.Canvas(ventana_carta)
        carta_canvas.pack()

        # Crear un Frame dentro del Canvas para organizar los platos en dos columnas
        platos_frame = tk.Frame(carta_canvas)
        carta_canvas.create_window((0, 0), window=platos_frame, anchor="nw")

        # Agregar una barra de desplazamiento vertical al Canvas
        scrollbar = tk.Scrollbar(ventana_carta, orient="vertical", command=carta_canvas.yview)
        carta_canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Agregar un controlador de eventos para el desplazamiento con la rueda del ratón
        carta_canvas.bind_all("<MouseWheel>", lambda event: carta_canvas.yview_scroll(-1*(event.delta//120), "units"))

        # Crear elementos de la carta (platos)
        platos = [
               {"nombre": "Café expreso", "precio": 3.000, "imagen": "1.png"},
{"nombre": "Whisky", "precio": 40.000, "imagen": "2.png"},
{"nombre": "Té negro", "precio": 7.000, "imagen": "3.png"},
{"nombre": "Coctel rainbow paradise", "precio": 50.000, "imagen": "4.png"},
{"nombre": "Coca cola", "precio": 5.000, "imagen": "5.png"},
{"nombre": "Vino", "precio": 40.000, "imagen": "6.png"},
{"nombre": "Limonada con menta", "precio": 7.000, "imagen": "7.png"},
{"nombre": "Botella de agua", "precio": 3.000, "imagen": "8.png"},
{"nombre": "Jugos naturales", "precio": 10.000, "imagen": "9.png"},
{"nombre": "Sushi", "precio": 30.000, "imagen": "10.png"},
{"nombre": "Hamburguesa", "precio": 30.000, "imagen": "11.png"},
{"nombre": "Tacos", "precio": 30.000, "imagen": "12.png"},
{"nombre": "Ensalada", "precio": 25.000, "imagen": "13.png"},
{"nombre": "Sopa de verduras", "precio": 20.000, "imagen": "14.png"},
{"nombre": "Pescado", "precio": 30.000, "imagen": "15.png"},
{"nombre": "Pechuga de pollo", "precio": 30.000, "imagen": "16.png"},
{"nombre": "Pizza Margherita", "precio": 40.000, "imagen": "17.png"},
{"nombre": "Pasta", "precio": 20.000, "imagen": "18.png"},
{"nombre": "Copa de helado", "precio": 12.000, "imagen": "19.png"},
{"nombre": "Cerveza", "precio": 5.000, "imagen": "20.png"},
            # Agregar más platos aquí
        ]

        self.cuentas_mesas[numero_mesa] = 0  # Inicializar la cuenta de la mesa

        text_mensajes = tk.Text(ventana_carta, height=5, width=40)
        text_mensajes.pack()

        for i, plato in enumerate(platos):
            nombre = plato["nombre"]
            precio = plato["precio"]
            imagen_path = os.path.join(self.script_dir, plato["imagen"])  # Ruta absoluta de la imagen

            self.crear_plato(platos_frame, numero_mesa, i, nombre, precio, imagen_path, text_mensajes)
        # Obtener el tamaño total de los platos
        carta_canvas.update_idletasks()
        carta_canvas.config(scrollregion=carta_canvas.bbox("all"))

        # Agregar un botón "Cerrar" para la ventana de la carta
        boton_cerrar = tk.Button(ventana_carta, text="Cerrar", command=ventana_carta.destroy)
        boton_cerrar.pack()

    def crear_plato(self, platos_frame, numero_mesa, plato_index, nombre, precio, imagen_path, text_mensajes):
        plato_frame = tk.Frame(platos_frame)
        plato_frame.grid(row=plato_index // 2, column=plato_index % 2, padx=10, pady=10)

        label = tk.Label(plato_frame, text=f"{nombre} - ${precio}")
        label.pack()

        imagen = Image.open(imagen_path)
        imagen = imagen.resize((100, 100))
        imagen = ImageTk.PhotoImage(imagen)
        imagen_label = tk.Label(plato_frame, image=imagen)
        imagen_label.image = imagen
        imagen_label.pack()

        boton_agregar = tk.Button(plato_frame, text="Agregar", command=lambda: self.agregar_a_cuenta(numero_mesa, plato_index, precio, text_mensajes))
        boton_agregar.pack()

    def agregar_a_cuenta(self, numero_mesa, plato_index, precio, text_mensajes):
        self.cuentas_mesas[numero_mesa] += precio
        mensaje = f"Se agregó ${precio} a la cuenta de Mesa {numero_mesa + 1}. Total: ${self.cuentas_mesas[numero_mesa]}\n"
        text_mensajes.insert(tk.END, mensaje)

        # Registrar el pedido en el diccionario de pedidos
        if numero_mesa not in self.pedidos:
            self.pedidos[numero_mesa] = []
        self.pedidos[numero_mesa].append({"plato": plato_index, "precio": precio})

        # Guardar los pedidos en el archivo JSON
        self.guardar_pedidos()

    def guardar_pedidos(self):
        # Guardar el diccionario de pedidos en un archivo JSON
        with open('pedidos.json', 'w') as file:
            json.dump(self.pedidos, file)

    def cerrar_ventana(self):
        self.root.destroy()

    def cargar_pedidos(self):
        # Cargar el diccionario de pedidos desde el archivo JSON
        if os.path.exists('pedidos.json'):
            with open('pedidos.json', 'r') as file:
                self.pedidos = json.load(file)

    def consultar_cuentas(self):
        ventana_consultar_cuentas = tk.Toplevel(self.root)
        ventana_consultar_cuentas.title("Consultar Cuentas")
        
        # Crear una etiqueta para seleccionar la mesa
        label_mesa = tk.Label(ventana_consultar_cuentas, text="Selecciona una mesa:")
        label_mesa.pack()

        # Crear un menú desplegable para seleccionar la mesa
        opciones_mesas = ["Mesa {}".format(i) for i in range(1, 21)]
        numero_mesa = tk.StringVar()
        menu_mesa = tk.OptionMenu(ventana_consultar_cuentas, numero_mesa, *opciones_mesas)
        menu_mesa.pack()

        # Crear un botón para consultar la cuenta
        boton_consultar = tk.Button(ventana_consultar_cuentas, text="Consultar Cuenta", command=lambda: self.mostrar_factura_consulta(numero_mesa.get()))
        boton_consultar.pack()

    def mostrar_factura_consulta(self, mesa_seleccionada):
        if not mesa_seleccionada:
            return

        mesa_numero = int(mesa_seleccionada.split()[-1])  # Obtener el número de mesa
        if mesa_numero < 1 or mesa_numero > 20:
            return

        total_cuenta = self.cuentas_mesas[mesa_numero - 1]
        platos_pedidos = self.pedidos.get(mesa_numero, [])

        factura_texto = f"Factura de la Mesa {mesa_numero}:\n"

        for pedido in platos_pedidos:
            plato_index = pedido["plato"]
            plato = platos[plato_index]
            nombre = plato["nombre"]
            precio = pedido["precio"]
            factura_texto += f"{nombre} - ${precio:.2f}\n"

        factura_texto += f"Subtotal: ${total_cuenta:.2f}\n"
        impuesto = total_cuenta * 0.12  # Suponiendo un impuesto del 12%
        factura_texto += f"Impuesto (12%): ${impuesto:.2f}\n"
        total_a_pagar = total_cuenta + impuesto
        factura_texto += f"Total a Pagar: ${total_a_pagar:.2f}"

        # Crear una nueva ventana para mostrar la factura
        ventana_factura = tk.Toplevel(self.root)
        ventana_factura.title(f"Factura de Mesa {mesa_numero}")
        
        factura_label = tk.Label(ventana_factura, text=factura_texto)
        factura_label.pack()

        # Agregar un botón "Cerrar" para la ventana de la factura
        boton_cerrar_factura = tk.Button(ventana_factura, text="Cerrar", command=ventana_factura.destroy)
        boton_cerrar_factura.pack()

def ejecutar_app():
    root = tk.Tk()
    app = MesaApp(root)
    root.mainloop()

if __name__ == "__main__":
    ejecutar_app()
