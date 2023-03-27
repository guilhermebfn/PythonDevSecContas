from Conta import Conta

class ContaCorrente(Conta):
    limite: float

    def __init__(self, id_conta: int, saldo: float, limite: float) -> None:
        super().__init__(id_conta, saldo)
        self.limite = limite

    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def sacar(self, valor: float) -> None:
        if self.saldo + self.limite < valor:
            raise ValueError("Valor maior que o permitido")

        self.saldo -= valor

        