from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self, args) -> None:
        pass

class Pessoa:
    def __init__(self, pessoaID, nome):
        self.pessoaID = pessoaID
        self.nome = nome

# receptor
class BancoPessoas:
    def __init__(self):
        self.pessoas = {}

    def new(self, pessoaID, nome):
        if pessoaID in self.pessoas:
            raise ValueError("ja existe uma pessoa com este id")
        self.pessoas[pessoaID] = Pessoa(pessoaID, nome)

    def delete(self, pessoaID):
        if pessoaID in self.pessoas:
            self.pessoas.pop(pessoaID)
        else:
            raise ValueError("id nao encontrado")

    def get(self, pessoaID):
        if pessoaID not in self.pessoas:
            raise ValueError("pessoa nao encontrada")
        
        return self.pessoas[pessoaID]
    
    def all(self):
        return list(self.pessoas.values())

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
