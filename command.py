from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self) -> None:
        pass

class Pessoa:
    pass

# receptor
class BancoPessoas:
    pass

class NewComando:
    pass

class DeleteComando:
    pass

class GetComando:
    pass

class AllComando:
    pass

class Executor:
    pass
