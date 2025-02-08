from ..interface import menu
from ..utils import encerrar_missao, esperar, limpar


def executar_m6():
  menu("Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾", "Exibir números de 1 a 10")

  while True:
    limpar()

    print("Exibindo números...")
    for i in range(1, 11):
      esperar(1)
      print(i)

    decisao = encerrar_missao()
    if (decisao):
      break
