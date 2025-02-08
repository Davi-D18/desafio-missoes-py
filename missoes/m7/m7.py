from ..interface import menu
from ..utils import encerrar_missao, esperar, limpar
from .operacoes import escolher_operacao


def executar_m7():
  menu("Missão 7: Organizando a Lista 📋", "organiza uma lista de números.")

  while True:
    limpar()
    try:
      print("1 - Crescente | 2 - Decrescente")
      operacao = int(input("Informe a operação que deseja fazer com uma lista: "))
    except ValueError:
      print("Você deve informar um número de acordo com a operação")
      esperar(2)
      continue

    lista_modificada = escolher_operacao(operacao)
    print(f"Lista modificada: {lista_modificada}")
    esperar(2)

    decisao = encerrar_missao()
    if (decisao):
      break

    