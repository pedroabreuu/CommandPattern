from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self, args) -> None:
        pass

class Pessoa:
    def __init__(self, pessoaID: int, nome: str) -> None:
        self.pessoaID = pessoaID
        self.nome = nome

    def __str__(self):
        return f"{self.pessoaID}: {self.nome}"

# receptor
class BancoPessoas:
    def __init__(self) -> None:
        self.pessoas = {}

    def new(self, pessoaID: int, nome: str) -> None:
        if pessoaID in self.pessoas:
            raise ValueError("ja existe uma pessoa com este id")
        self.pessoas[pessoaID] = Pessoa(pessoaID, nome)

    def delete(self, pessoaID: int) -> None:
        if pessoaID in self.pessoas:
            self.pessoas.pop(pessoaID)
        else:
            raise ValueError("id nao encontrado")

    def get(self, pessoaID: int) -> Pessoa:
        if pessoaID not in self.pessoas:
            raise ValueError("pessoa nao encontrada")
        
        return self.pessoas[pessoaID]
    
    def all(self) -> list[Pessoa]:
        return list(self.pessoas.values())

class NewComando(Comando):
    def __init__(self, banco: BancoPessoas) -> None:
        self.banco = banco

    def executar(self, args) -> None:
        if len(args) != 2: # se nao foi passado <id> e <nome>
            raise ValueError("uso incorreto, usar new <id> <nome>")

        pessoaID = int(args[0])
        nome = args[1]
        self.banco.new(pessoaID, nome)

class DeleteComando(Comando):
    def __init__(self, banco) -> None:
        self.banco = banco

    def executar(self, args) -> None:
        if len(args) != 1:
            raise ValueError("uso incorreto, usar delete <id>")

        pessoaID = int(args[0])
        self.banco.delete(pessoaID)

class GetComando(Comando):
    def __init__(self, banco) -> None:
        self.banco = banco

    def executar(self, args) -> None:
        if len(args) != 1:
            raise ValueError("uso incorreto, usar get <id>")

        pessoaID = int(args[0])
        pessoa = self.banco.get(pessoaID)
        print(pessoa)

class AllComando(Comando):
    def __init__(self, banco) -> None:
        self.banco = banco

    def executar(self, args) -> None:
        if len(args) != 0:
            raise ValueError("uso incorreto, usar apenas all")

        pessoas = self.banco.all()
        for pessoa in pessoas:
            print(pessoa)

class Executor:
    def __init__(self, banco: BancoPessoas) -> None:
        self.comandos: Dict[str, Comando] = {
            "new": NewComando(banco),
            "delete": DeleteComando(banco),
            "get": GetComando(banco),
            "all": AllComando(banco),
        }

    def executar(self, nome_comando: str, args: List[str]) -> None:
        if nome_comando not in self.comandos:
            raise ValueError(f"comando desconhecido: {nome_comando}")

        comando = self.comandos[nome_comando]
        comando.executar(args)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("uso correto: python command.py <comando> [args]")
        sys.exit(1)

    nome_comando: str = sys.argv[1]
    args: List[str] = sys.argv[2:]

    banco: BancoPessoas = BancoPessoas()
    executor: Executor = Executor(banco)

    try:
        executor.executar(nome_comando, args)
    except ValueError as erro:
        print(f"erro: {erro}")
