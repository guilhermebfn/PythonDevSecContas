from Conta import Conta

class ContaCorrente(Conta):
    _limite: float

    def __init__(self, id_conta: int, saldo: float, limite: float) -> None:
        super().__init__(id_conta, saldo)
        self._limite = limite

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

        