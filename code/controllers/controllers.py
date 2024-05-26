from abc import ABC, abstractmethod
import sqlite3

#Definição de uma classe para conexão com o banco de dados
class ConectaBanco:
    def __init__(self, db_name):
        self.db_name = db_name

    #Método para obter uma conexão com o banco de dados SQLite
    def get_conexao(self):
        return sqlite3.connect(self.db_name)

#Definição da Classe Cliente
class Cliente:
    def __init__(self, nome, email, empresa, telefone):
        self.nome = nome
        self.email = email
        self.empresa = empresa
        self.telefone = telefone

#Definição da classe abstrata ClienteDAO com métodos abstratos para operaçõpes com clientes
class ClienteDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    #Métodos abstratos para definir as operações
    @abstractmethod
    def inserir(self, cliente: Cliente):
        pass

    @abstractmethod
    def visualizar(self, cliente_id):
        pass

    @abstractmethod
    def alterar(self, cliente):
        pass

    @abstractmethod
    def excluir(self, cliente_id):
        pass

#Implementação do DAO para clientes utilizando SQLite
class SQLiteClienteDAO(ClienteDAO):
    #Método para criar a tabela de clientes no banco de dados
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        empresa TEXT NOT NULL,
                        telefone TEXT NOT NULL)''')
        conexao.commit()

    #Implementação do método inserir, que adiciona um cliente ao banco de dados
    def inserir(self, cliente: Cliente):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO clientes (nome,email,empresa,telefone) VALUES (?,?,?,?)''',
                        (cliente.nome, cliente.email, cliente.empresa, cliente.telefone))
        conexao.commit()

    #Implementação do método visualizar, que retorna um cliente baseado em seu ID
    def visualizar(self, cliente_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM clientes WHERE id = (?)', (cliente_id,))
        return cursor.fetchall()

    #Implementação do método alterar, que atualiza os dados de um cliente
    def alterar(self, cliente):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE clientes SET nome = (?) WHERE id = (?)', (cliente.nome, cliente.id))

    #Implementação do método excluir, que remove um cliente do banco de dados
    def excluir(self, cliente_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM clientes WHERE id = (?)', (cliente_id,))
        conexao.commit()

#Classe ClienteController para gerenciar operações relacionadas a clientes
class ClienteController():
    def __init__(self):
        self.conexao = ConectaBanco("clientes.db")
        self.cliente_dao = SQLiteClienteDAO(self.conexao)
        self.cliente_dao.criar_tabela()

    #Método para criar um novo cliente
    def criar_cliente(self, cliente: Cliente):
        self.cliente_dao.inserir(cliente)

    #Método para visualizar um cliente específico
    def visualizar_cliente(self, cliente_id):
        return self.cliente_dao.visualizar(cliente_id)

    #Método para alterar os dados de um cliente
    def alterar_cliente(self, cliente):
        self.cliente_dao.alterar(cliente)

    #Método para excluir um cliente
    def excluir_cliente(self, cliente_id):
        self.cliente_dao.excluir(cliente_id)

#Implementação da mesma estrutura criada para o banco de dados de clientes para Usuários, Problemas e Chamados
class Usuario:
    def __init__(self, nome, email, senha, cargo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo

class UsuarioDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def inserir(self, usuario):
        pass

    @abstractmethod
    def visualizar(self, usuario_id):
        pass

    @abstractmethod
    def alterar(self, usuario):
        pass

    @abstractmethod
    def excluir(self, usuario_id):
        pass

class SQLiteUsuarioDAO(UsuarioDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        senha TEXT NOT NULL,
                        cargo TEXT NOT NULL)''')
        conexao.commit()

    def inserir(self, usuario):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO usuarios (nome,email,senha,cargo) VALUES (?,?,?,?)''',
                        (usuario.nome, usuario.email, usuario.senha, usuario.cargo))
        conexao.commit()

    def visualizar(self, usuario_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE id = (?)', (usuario_id,))
        return cursor.fetchall()

    def alterar(self, usuario):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE usuarios SET nome = (?) WHERE id = (?)', (usuario.nome, usuario.id))

    def excluir(self, usuario_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM usuarios WHERE id = (?)', (usuario_id,))
        conexao.commit()

class UsuarioController():
    def __init__(self):
        self.conexao = ConectaBanco("usuarios.db")
        self.usuario_dao = SQLiteUsuarioDAO(self.conexao)
        self.usuario_dao.criar_tabela()

    def criar_usuario(self, usuario):
        self.usuario_dao.inserir(usuario)

    def visualizar_usuario(self, usuario_id):
        return self.usuario_dao.visualizar(usuario_id)

    def alterar_usuario(self, usuario):
        self.usuario_dao.alterar(usuario)

    def excluir_usuario(self, usuario_id):
        self.usuario_dao.excluir(usuario_id)

class Problema:
    def __init__(self, descricao, sla):
        self.descricao = descricao
        self.sla = sla

class ProblemaDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def inserir(self, problema):
        pass

    @abstractmethod
    def visualizar(self, problema_id):
        pass

    @abstractmethod
    def alterar(self, problema):
        pass

    @abstractmethod
    def excluir(self, problema_id):
        pass

class SQLiteProblemaDAO(ProblemaDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS problemas
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        descricao TEXT NOT NULL,
                        sla INT NOT NULL)''')
        conexao.commit()

    def inserir(self, problema):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO problemas (descricao,sla) VALUES (?,?)''',
                        (problema.descricao, problema.sla))
        conexao.commit()

    def visualizar(self, problema_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM problemas WHERE id = (?)', (problema_id,))
        return cursor.fetchall()

    def alterar(self, problema):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE problemas SET descricao = (?) WHERE id = (?)', (problema.descricao, problema.id))

    def excluir(self, problema_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM problemas WHERE id = (?)', (problema_id,))
        conexao.commit()

class ProblemaController():
    def __init__(self):
        self.conexao = ConectaBanco("problemas.db")
        self.problema_dao = SQLiteProblemaDAO(self.conexao)
        self.problema_dao.criar_tabela()

    def criar_problema(self, problema):
        self.problema_dao.inserir(problema)

    def visualizar_problema(self, problema_id):
        return self.problema_dao.visualizar(problema_id)

    def alterar_problema(self, problema):
        self.problema_dao.alterar(problema)

    def excluir_problema(self, problema_id):
        self.problema_dao.excluir(problema_id)

class Chamado:
    def __init__(self, titulo, descricao, status, data_abertura, data_max, data_fechamento):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_abertura = data_abertura
        self.data_max = data_max
        self.data_fechamento = data_fechamento

class ChamadoDAO(ABC):
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao

    @abstractmethod
    def abrir(self, chamado):
        pass

    @abstractmethod
    def atribuir_atendente(self, chamado):
        pass

    @abstractmethod
    def alterar_status(self, chamado):
        pass

    @abstractmethod
    def fechar(self, chamado):
        pass

    @abstractmethod
    def visualizar(self, chamado_id):
        pass

    @abstractmethod
    def alterar(self, chamado):
        pass

    @abstractmethod
    def excluir(self, chamado_id):
        pass

class SQLiteChamadoDAO(ChamadoDAO):
    def criar_tabela(self):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS chamados
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        descricao TEXT NOT NULL,
                        status TEXT NOT NULL,
                        data_abertura DATE NOT NULL,
                        data_max DATE NOT NULL,
                        data_fechamento DATE NOT NULL)''')
        conexao.commit()

    #Método para inserir um novo chamado no banco de dados
    def abrir(self, chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO chamados (titulo,descricao,status,data_abertura,data_max,data_fechamento) VALUES (?,?,?,?,?,?)''',
                        (chamado.titulo, chamado.descricao, chamado.status, chamado.data_abertura, chamado.data_max, chamado.data_fechamento))
        conexao.commit()

    #Método que atribui um atendente a um chamado
    def atribuir_atendente(self, chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE chamados SET usuarios(id) = (?) WHERE id = (?)', (chamado.atendente_id, chamado.id))
        conexao.commit()

    #Método que atualiza o status de um chamado no banco de dados
    def alterar_status(self, chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE chamados SET status = (?) WHERE id = (?)', (chamado.status, chamado.id))
        conexao.commit()

    #Método que marca um chamado como fechado no banco de dados
    def fechar(self, chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE chamados SET status = "Fechado" WHERE id = (?)', (chamado.id,))
        conexao.commit()

    #Método que busca um chamado no banco de dados de acordo com o respectivo ID
    def visualizar(self, chamado_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM chamados WHERE id = (?)', (chamado_id,))
        return cursor.fetchall()

    #Método que atualiza os dados de um chamado no banco de dados
    def alterar(self, chamado):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE chamados SET titulo = (?) WHERE id = (?)', (chamado.titulo, chamado.id))
        conexao.commit()

    #Método que remove um chamado do banco de dados
    def excluir(self, chamado_id):
        conexao = self.db_conexao.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM chamados WHERE id = (?)', (chamado_id,))
        conexao.commit()

class ChamadoController():
    def __init__(self):
        self.conexao = ConectaBanco("chamados.db")
        self.chamado_dao = SQLiteChamadoDAO(self.conexao)
        self.chamado_dao.criar_tabela()

    def criar_chamado(self, chamado):
        self.chamado_dao.abrir(chamado)

    def atribuir_atendente_chamado(self, chamado):
        self.chamado_dao.atribuir_atendente(chamado)

    def alterar_status_chamado(self, chamado):
        self.chamado_dao.alterar_status(chamado)

    def fechar_chamado(self, chamado):
        self.chamado_dao.fechar(chamado)

    def visualizar_chamado(self, chamado_id):
        return self.chamado_dao.visualizar(chamado_id)

    def alterar_chamado(self, chamado):
        self.chamado_dao.alterar(chamado)

    def excluir_chamado(self, chamado_id):
        self.chamado_dao.excluir(chamado_id)