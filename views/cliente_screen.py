from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class ClienteScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.usuario_controller = UsuarioController()
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.root.title('Trabalho de POO - Tela do Cliente')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes de login
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=200)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteScreen(root)
    root.mainloop()