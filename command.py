from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self, args) -> None:
        pass

class Pessoa:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

# receptor
class BancoPessoas:
    pass

class NewComando(Comando):
    def __init__(self, banco):
        self.banco = banco

    def executar(self, args):
        pass

class DeleteComando(Comando):
    def __init__(self, banco):
        self.banco = banco

    def executar(self, args):
        pass

class GetComando(Comando):
    def __init__(self, banco):
        self.banco = banco

    def executar(self, args):
        pass

class AllComando(Comando):
    def __init__(self, banco):
        self.banco = banco

    def executar(self, args):
        pass

class Executor:
    pass
