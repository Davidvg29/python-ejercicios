from tkinter import *

ventana = Tk()
ventana.title("Manual de usuario:")
ventana.geometry("800x400")  # Tamaño de la ventana
ventana.config(bg="gray")  # Color de la ventana

# Configurar el ícono del sistema
ventana.iconbitmap(r"E:\Cosas para pc\Programacion\python-ejercicios\proyecto final\juan\asistencia.ico")

# Crear el área de texto
texto_ayuda = tk.Text(ventana, wrap=tk.WORD, font=("Helvetica", 12), bg="lightgray")
texto_ayuda.pack(expand=True, fill="both")

# Contenido del manual
manual = """
Manual de Usuario: Sistema de Asistencia Punto Digital Banda del Río Salí

Introducción
Este manual tiene como objetivo guiarte en el uso del Sistema de Asistencia del Punto Digital Banda del Río Salí. Este sistema está diseñado para registrar de forma eficiente la circulación de alumnos, facilitando la gestión administrativa y brindando datos precisos sobre la asistencia.

Funcionalidades Principales
- Registro de alumnos: Ingresar los datos personales de cada alumno (nombre completo, género, etc.).
- Registro de asistencia: Registrar la fecha, hora de entrada y salida de cada alumno.
- Generación de reportes: Obtener informes detallados sobre la asistencia de los alumnos, incluyendo:
  - Listado de alumnos por día.
  - Cantidad de alumnos por género.
  - Movimientos mensuales.
- Consulta de información: Buscar información específica sobre un alumno o un período determinado.

Soporte Técnico
En caso de dudas o problemas técnicos, comunícate con el equipo de soporte técnico a través del siguiente correo electrónico: bandadelriosali@puntodigital.gob.ar
"""
texto_ayuda.insert(tk.END, manual)

ventana.mainloop()
