from ..interface import loading, menu
from ..utils import encerrar_missao, esperar, limpar


def somar(numero1, numero2):
  return numero1 + numero2

def executar_m4():
  menu("Missão 4: Restaurando a Identificação de Números")

  while True:
    limpar()
    numero1 = int(input("Informe um número para somar: "))
    numero2 = int(input("Informe outro número para somar: "))

    loading("Somando")
    print(f"Seu resultado foi: {somar(numero1, numero2)}")
    esperar(1)

    decisao = encerrar_missao()
    if (decisao):
      break

