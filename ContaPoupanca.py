from Conta import Conta

class ContaPoupanca(Conta):
    _taxa_de_rendimento_ao_ano: float

    def __init__(self, taxa_de_rendimento_ao_ano: float) -> None:
        super().__init__()
        self._taxa_de_rendimento_ao_ano = taxa_de_rendimento_ao_ano / 100 # Taxa passada como porcentagem

    def get_id_conta(self) -> int:
        return self._id_conta

    def get_saldo(self) -> float:
        return self._saldo

    def get_taxa_de_rendimento_ao_ano(self) -> float:
        return self._taxa_de_rendimento_ao_ano

    def set_taxa_de_rendimento_ao_ano(self, nova_taxa: float) -> None:
        self._taxa_de_rendimento_ao_ano = nova_taxa

    def depositar(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("Não é permitido depositar valores negativos")
        
        self._saldo += valor

    def sacar(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("Não é permitido sacar valores negativos")
        
        if self._saldo < valor:
            raise ValueError("Valor maior que o permitido")

        self._saldo -= valor

    def verificar_rendimento_ao_ano(self, tempo: int, tipo: str) -> float:
        if tipo in ["ano", "a"]:
            taxa = self._taxa_de_rendimento_ao_ano
        elif tipo in ["mes", "mês", "M"]:
            taxa = self._taxa_de_rendimento_ao_ano ** (1 / 12)
        elif tipo in ["dia", "d"]:
            taxa = self._taxa_de_rendimento_ao_ano ** (1 / 365)
        elif tipo in ["hora", "h"]:
            taxa = self._taxa_de_rendimento_ao_ano ** (1 / (365 * 24))
        elif tipo in ["minuto", "min", "m"]:
            taxa = self._taxa_de_rendimento_ao_ano ** (1 / (365 * 24 * 60))
        elif tipo in ["segundo", "seg", "s"]:
            taxa = self._taxa_de_rendimento_ao_ano ** (1 / (365 * 24 * 60 * 60))
        
        return self._saldo * ((1 + taxa) ** tempo)
