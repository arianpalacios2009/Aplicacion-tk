import tkinter as tk

ventana = tk.Tk()
ventana.title("Lab.app")
ventana.geometry("320x400")
ventana.resizable(False,False)

titulo_labapp = tk.Label(ventana, text= "roblox", font= "Chango", fg= "blue")
titulo_labapp.pack(pady=15)

etiqueta_nombre = tk.Label(ventana, text="Introduce tu usuario:")
etiqueta_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

etiqueta_contrasena= tk.Label(ventana, text="Introduce tu contraseña:")
etiqueta_contrasena.pack(pady=5)
entrada_contrasena = tk.Entry(ventana)
entrada_contrasena.pack(pady=5)

usuario_correcto = "odra_400"
contrasena_correcta = "odra_400_"

def iniciar_sesion():
    nombre_usuario = entrada_nombre.get()
    contrasena = entrada_contrasena.get()
    if nombre_usuario == usuario_correcto and contrasena == contrasena_correcta:
        saludo.config(text=f"¡Inicio de sesion exitoso!")
    else:
        saludo.config(text=f"¡Inicio de sesion incorrecto!")


boton = tk.Button(ventana, text="Confirmar",bg= "green",  command=iniciar_sesion)
boton.pack(pady=10)

saludo = tk.Label(ventana, text="")
saludo.pack()

ventana.mainloop()