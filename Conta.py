from abc import abstractmethod, ABC

class Conta(ABC):
    _id_conta: int
    _saldo: float

    def __init__(self, id_conta: int, saldo: float) -> None:
        self._id_conta = id_conta
        self._saldo = saldo

    @abstractmethod
    def depositar(self, valor: float) -> None:
        pass

    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass
