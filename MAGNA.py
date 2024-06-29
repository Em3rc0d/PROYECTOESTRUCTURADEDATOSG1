import tkinter as tk
from tkinter import ttk
import subprocess

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto Magna")
        
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg='#2C3E50')
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=1, fill="both", padx=20, pady=20)

        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), padding=10)
        style.configure('TFrame', background='#2C3E50')

        title_label = tk.Label(self.main_frame, text="Proyecto Magna", font=('Helvetica', 18, 'bold'), bg='#2C3E50', fg='#ECF0F1')
        title_label.pack(pady=10)

        # Crear botones para abrir los main de cada proyecto
        self.create_project_button(self.main_frame, "Abrir Proyecto 1", "proyecto-alejandro-original/main.py")
        self.create_project_button(self.main_frame, "Abrir Proyecto 2", "proyectoED-main/gui.py")
        self.create_project_button(self.main_frame, "Abrir Proyecto 3", "jorigito_proyecto_luzmila.py")
        self.create_project_button(self.main_frame, "Abrir Proyecto 4", "PROYECTO_LUZMILA_fabrizio_raul.py")

    def create_project_button(self, frame, button_text, script_path):
        button = ttk.Button(frame, text=button_text, command=lambda: self.open_project(script_path), style='TButton')
        button.pack(pady=10)

    def open_project(self, script_path):
        # Cambia esta ruta por la ruta de tu ejecutable de Python
        python_executable = r"C:\Users\farid\AppData\Local\Programs\Python\Python312\python.exe"
        subprocess.Popen([python_executable, script_path], shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
