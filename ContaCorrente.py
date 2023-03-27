from Conta import Conta

class ContaCorrente(Conta):
    _limite: float

    def __init__(self, id_conta: int, saldo: float, limite: float) -> None:
        super().__init__(id_conta, saldo)
        self._limite = limite

    def get_id_conta(self) -> int:
        return self._id_conta

    def get_saldo(self) -> float:
        return self._saldo

    def get_limite(self) -> float:
        return self._limite

    def set_limite(self, valor: float) -> None:
        self._limite = valor

    def depositar(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("Não é permitido depositar valores negativos")

        self._saldo += valor

    def sacar(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("Não é permitido sacar valores negativos")
        
        if self._saldo + self._limite < valor:
            raise ValueError("Valor maior que o permitido")

        self._saldo -= valor
