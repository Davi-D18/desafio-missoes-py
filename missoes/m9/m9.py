from ..interface import loading, menu
from ..utils import encerrar_missao, esperar, limpar


def dobro_numero(numero1):
  return numero1 * 2

def executar_m9():
  menu("Missão 9: Calculando Dobro de um Número 🛠️", "Calcula o dobro de um número informado")

  while True:
    limpar()
    numero = float(input("Informe um número: "))

    loading("Calculando", 1)
    resultado = dobro_numero(numero)
    print(f"O dobro de {numero} é {resultado}")
    esperar(2)

    decisao = encerrar_missao()

    if (decisao):
      break