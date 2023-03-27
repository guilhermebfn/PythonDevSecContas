from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Conta corrente

print("Criação de conta corrente com saldo de 400 reais e limite de 200 reais")
conta_corrente = ContaCorrente(1, 400., 200.)

print(f"Antes do depósito: {conta_corrente.get_saldo()}")
conta_corrente.depositar(50.)
print(f"Depois do depósito de 50 reais: {conta_corrente.get_saldo()}")

print("Sacando 100 reais")
conta_corrente.sacar(100.)
print(f"Depois do saque de 100 reais: {conta_corrente.get_saldo()}")

print("Tentando sacar -100 reais")
try:
    conta_corrente.sacar(-100)
except:
    print("Não foi possível realizar o saque de valor negativo")

print("Sacando 400 reais")
conta_corrente.sacar(400.)
print(f"Depois do saque de 400 reais: {conta_corrente.get_saldo()}")

print("Tentando sacar 1000 reais")
try:
    conta_corrente.sacar(1000.)
except:
    print("Não foi possível realizar o saque que excede o limite")
    print(f"Limite: {conta_corrente.get_limite()}")

print("Aumentando o limite para 10000")
conta_corrente.set_limite(10000.)
print(f"Novo limite: {conta_corrente.get_limite()}")

print("Sacando 1000 reais")
conta_corrente.sacar(1000.)
print(f"Depois do saque de 1000 reais: {conta_corrente.get_saldo()}")

print("")

## Conta poupança

print("Criação de conta poupança com saldo de 400 reais e taxa de rendimento ao ano de 20%")
conta_poupanca = ContaPoupanca(1, 400., 20.)

print(f"Antes do depósito: {conta_poupanca.get_saldo()}")
conta_poupanca.depositar(50.)
print(f"Depois do depósito de 50 reais: {conta_poupanca.get_saldo()}")

print("Sacando 100 reais")
conta_poupanca.sacar(100.)
print(f"Depois do saque de 100 reais: {conta_poupanca.get_saldo()}")

print("Tentando sacar -100 reais")
try:
    conta_poupanca.sacar(-100)
except:
    print("Não foi possível realizar o saque de valor negativo")

print("Tentando sacar 1000 reais")
try:
    conta_poupanca.sacar(1000.)
except:
    print("Não foi possível realizar o saque que excede o saldo")

print(f"Taxa de rendimento anual: {conta_poupanca.get_taxa_de_rendimento_ao_ano() * 100}%")

print(f"Valor atual do saldo: {conta_poupanca.get_saldo()}")
print(f"Valor do saldo após 1 ano: {conta_poupanca.verificar_rendimento_ao_ano(1, 'ano'):.2f}")
print(f"Valor do saldo após 2 meses: {conta_poupanca.verificar_rendimento_ao_ano(2, 'mes'):.2f}")
print(f"Valor do saldo após 15 dias: {conta_poupanca.verificar_rendimento_ao_ano(15, 'dia'):.2f}")
print(f"Valor do saldo após 24 horas: {conta_poupanca.verificar_rendimento_ao_ano(24, 'hora'):.2f}")
print(f"Valor do saldo após 60 minutos: {conta_poupanca.verificar_rendimento_ao_ano(60, 'minuto'):.2f}")
print(f"Valor do saldo após 3600 segundos: {conta_poupanca.verificar_rendimento_ao_ano(3600, 'segundo'):.2f}")