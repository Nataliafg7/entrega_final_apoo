import tkinter as tk
import json
from tkinter import PhotoImage
from menu_mesas import MenuMesas  # Importa la clase MenuMesas desde menu_mesas.py
from menu_ventas import MenuVentas
class Mesero:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Beef Station")
        image = PhotoImage(file="imagen.gif")
        image = image.subsample(5)

        # Crear una etiqueta (Label) para mostrar la imagen en la parte superior de la ventana
        image_label = tk.Label(root, image=image)
        image_label.image = image  # Guardar una referencia para evitar que la imagen sea eliminada
        image_label.pack()

        self.label_usuario = tk.Label(root, text="Usuario:")
        self.label_usuario.pack()
        
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()
        
        self.label_password = tk.Label(root, text="Contraseña:")
        self.label_password.pack()
        
        self.entry_password = tk.Entry(root, show="*")  # Para ocultar la contraseña
        self.entry_password.pack()
        
        self.button_crear_cuenta = tk.Button(root, text="Crear Cuenta", command=self.crear_cuenta)
        self.button_crear_cuenta.pack()
        
        self.button_iniciar_sesion = tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.button_iniciar_sesion.pack()
        
        self.bienvenida_label = tk.Label(root, text="")
        self.bienvenida_label.pack()
        
        self.button_cerrar_sesion = tk.Button(root, text="Cerrar Sesión", command=self.cerrar_sesion, state="disabled")
        self.button_cerrar_sesion.pack(side="right")

        
        self.button_mesas = None  # Añade un atributo para el botón "Mesas"
        
        # Crear instancias de MenuMesas y MenuVentas
        self.menu_mesas = MenuMesas(root)
        self.menu_ventas = MenuVentas(root)
        
        # Mantener un seguimiento del usuario actual
        self.usuario_actual = None
        self.sesion_iniciada = False
    def crear_cuenta(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        # Cargar datos existentes de usuarios desde el archivo JSON
        try:
            with open('usuarios.json', 'r') as file:
                usuarios = json.load(file)
        except FileNotFoundError:
            usuarios = {}
        
        if usuario in usuarios:
            self.mostrar_mensaje("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        else:
            # Agregar el nuevo usuario
            usuarios[usuario] = password
        
            # Guardar los datos actualizados en el archivo JSON
            with open('usuarios.json', 'w') as file:
                json.dump(usuarios, file)
        
            self.mostrar_mensaje("Cuenta creada con éxito.")
        
        self.entry_usuario.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        
    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        # Cargar datos existentes de usuarios desde el archivo JSON
        try:
            with open('usuarios.json', 'r') as file:
                usuarios = json.load(file)
        except FileNotFoundError:
            usuarios = {}
        
        if usuario in usuarios and usuarios[usuario] == password:
            self.usuario_actual = usuario
            self.sesion_iniciada = True
            self.ocultar_campos_usuario_contraseña()
            self.mostrar_botones_menu()
            self.mostrar_mensaje(f"Bienvenido, {usuario}!")
        else:
            self.mostrar_mensaje("Credenciales incorrectas. Inténtelo de nuevo.")
        
        self.entry_usuario.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        

    def cerrar_sesion(self):
        self.sesion_iniciada = False
        self.mostrar_campos_usuario_contraseña()
        self.menu_mesas.ocultar()
        self.menu_ventas.ocultar()
        self.mostrar_mensaje("")
        self.usuario_actual = None
        self.ocultar_botones_menu()
        self.ocultar_boton_mesas()  # Oculta el botón "Mesas" al cerrar la sesión
        self.ocultar_boton_ventas()
        self.ocultar_boton_cerrar()
    def ocultar_botones_menu(self):
        self.menu_mesas.ocultar()
        self.menu_ventas.ocultar()

    def mostrar_campos_usuario_contraseña(self):
        self.label_usuario.pack()
        self.entry_usuario.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_crear_cuenta.pack()
        self.button_iniciar_sesion.pack()
        self.button_cerrar_sesion.config(state="disabled")

    def ocultar_campos_usuario_contraseña(self):
        self.label_usuario.pack_forget()
        self.entry_usuario.pack_forget()
        self.label_password.pack_forget()
        self.entry_password.pack_forget()
        self.button_crear_cuenta.pack_forget()
        self.button_iniciar_sesion.pack_forget()
        self.button_cerrar_sesion.config(state="active")

    def mostrar_botones_menu(self):
        menu_frame = tk.Frame(self.root)  # Crear un nuevo marco para el menú
        menu_frame.pack()
        
        self.button_mesas = tk.Button(menu_frame, text="Mesas", command=self.mostrar_menu_mesas)
        self.button_mesas.pack(side="left")
        
        self.button_ventas = tk.Button(menu_frame, text="Ventas", command=self.mostrar_menu_ventas)
        self.button_ventas.pack(side="left")

    def mostrar_menu_mesas(self):
        self.menu_ventas.ocultar()
        self.menu_mesas.mostrar()

    def mostrar_menu_ventas(self):
        self.menu_mesas.ocultar()
        self.menu_ventas.mostrar()

    def mostrar_mensaje(self, mensaje):
        self.bienvenida_label.config(text=mensaje)

    def ocultar_boton_mesas(self):
        if self.button_mesas:
            self.button_mesas.pack_forget()
    def ocultar_boton_ventas(self):
        if self.button_ventas:
            self.button_ventas.pack_forget()
    def ocultar_boton_cerrar(self):
            if self.button_cerrar_sesion:
                self.button_cerrar_sesion.pack_forget()



