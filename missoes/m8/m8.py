from ..interface import menu
from ..utils import encerrar_missao, esperar, limpar
from .funcoes import adicionar_nomes, exibir_nomes, tupla_nomes


def executar_m8():
  global tupla_nomes
  
  menu("Missão 8: Acessando os Registros de Alunos 🏷️", "Exibe o primeiro e último nome de uma tupla")

  while True:
    limpar()
    print(tupla_nomes)
    print("")
    print("1 - Exibir nomes  |  2 - Adicionar nome")

    escolha = int(input("Informe o número da operação: "))

    match escolha:
      case 1:
        exibir_nomes()
      case 2:
        tupla_nomes = adicionar_nomes()
      case _:
        print("Opção inválida")
        esperar(1)
        continue

    decisao = encerrar_missao()
    if (decisao):
      break

