import tkinter as tk

ventana = tk.Tk()
ventana.title("Lab.app")
ventana.geometry("320x400")
ventana.resizable(False,False)

frame1 = tk.Frame(ventana,bg="pink",bd=5,relief="groove",width="250",height="300") 
frame1.pack(pady=20)

titulo_labapp = tk.Label(frame1, text= "roblox", font= "Chango", bg="pink")
titulo_labapp.pack(pady=15)

etiqueta_nombre = tk.Label(frame1, text="Introduce tu usuario:")
etiqueta_nombre.pack(pady=5)
entrada_nombre = tk.Entry(frame1)
entrada_nombre.pack(pady=5)

etiqueta_contrasena= tk.Label(frame1, text="Introduce tu contraseña:")
etiqueta_contrasena.pack(pady=5)
entrada_contrasena = tk.Entry(frame1)
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


boton = tk.Button(frame1, text="Confirmar",bg= "green",  command=iniciar_sesion)
boton.pack(pady=10)

saludo = tk.Label(frame1, text="")
saludo.pack()

ventana.mainloop()