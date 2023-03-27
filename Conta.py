from abc import abstractmethod, ABC

class Conta(ABC):
    id_conta: int
    saldo: float

    def __init__(self, id_conta: int, saldo: float) -> None:
        self.id_conta = id_conta
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor: float) -> None:
        pass

    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass
