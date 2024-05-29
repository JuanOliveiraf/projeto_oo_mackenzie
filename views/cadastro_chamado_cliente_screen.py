from models import Cliente, Usuario, Problema, Chamado
from controllers import ClienteController, UsuarioController, ProblemaController, ChamadoController
import tkinter as tk
from tkinter import messagebox

class CadastroChamadoClienteScreen:

    def __init__(self, root) -> None:
        self.root = root
        self.selected_id_chamado = None
        self.bold_font = ('Helvetica', 12, 'bold')
        self.title_font = ('Helvetica', 14, 'bold')
        self.cliente_controller = ClienteController()
        self.chamado_controller = ChamadoController()
        self.usuario_controller = UsuarioController()
        self.problema_controller = ProblemaController()
        self.root.title('Trabalho de POO - Tela de Cadastro do Chamado do Cliente')
        self.root.geometry('1280x720')
        
        # Cria um frame para os componentes da tela
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.id_chamado_label = tk.Label(self.frame, text='ID do chamado:', font=self.bold_font, anchor='w')
        self.id_chamado_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.id_chamado_entry = tk.Entry(self.frame, width=30, state='disabled')
        self.id_chamado_entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

        # Campo ID do cliente
        self.id_cliente_label = tk.Label(self.frame, text='ID do cliente:', font=self.bold_font, anchor='w')
        self.id_cliente_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.id_cliente_entry = tk.Entry(self.frame, width=30, state='disabled')
        self.id_cliente_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        # Campo Nome
        self.nome_label = tk.Label(self.frame, text='Nome:', font=self.bold_font, anchor='w')
        self.nome_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.nome_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.nome_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

        # Campo Empresa
        self.empresa_label = tk.Label(self.frame, text='Empresa:', font=self.bold_font, anchor='w')
        self.empresa_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.empresa_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.empresa_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        # Campo Telefone
        self.telefone_label = tk.Label(self.frame, text='Telefone:', font=self.bold_font, anchor='w')
        self.telefone_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.telefone_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.telefone_entry.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

        # Campo Título
        self.titulo_label = tk.Label(self.frame, text='Título:', font=self.bold_font, anchor='w')
        self.titulo_label.grid(row=0, column=3, padx=10, pady=10, sticky='w')
        self.titulo_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.titulo_entry.grid(row=0, column=4, padx=10, pady=10, sticky='ew')

        # Campo Descrição do Relato
        self.descricao_label = tk.Label(self.frame, text='Descrição do Relato:', font=self.bold_font, anchor='w')
        self.descricao_label.grid(row=1, column=3, padx=10, pady=10, sticky='w')
        self.descricao_entry = tk.Entry(self.frame, width=30, fg='grey')
        self.descricao_entry.grid(row=1, column=4, padx=10, pady=10, sticky='ew')

        # Botão de cadastrar chamado
        self.cadastrar_button = tk.Button(self.frame, text='Cadastrar Chamado', command=self.cadastrar_chamado, bg='green', fg='white')
        self.cadastrar_button.grid(row=5, column=1, pady=20, padx=10, sticky='ew')

        # Botão de cancelar
        self.cancelar_button = tk.Button(self.frame, text='Cancelar', command=self.cancelar, bg='#E57373', fg='white')
        self.cancelar_button.grid(row=5, column=4, pady=20, padx=10, sticky='ew') 
        
    def cadastrar_chamado(self) -> None:
        pass

    def cancelar(self) -> None:
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroChamadoClienteScreen(root)
    root.mainloop()