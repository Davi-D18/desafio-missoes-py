from ..interface import loading, menu
from ..utils import encerrar_missao, esperar, limpar


def contar_letras(nome):
  """Conta as letras de um nome."""
  return len(nome)

def executar_m10():
  menu("Missão 10: Contando Letras 🔄", "conta as letras de um nome.")

  while True:
    limpar()
    nome = input("Informe seu nome: ").title().strip()

    if nome == "":
      print("Nome inválido. Tente novamente.")
      esperar(1)
      continue

    loading("Contando letras", 1)
    letras_contadas = contar_letras(nome)
    print(f"O nome {nome} tem {letras_contadas} letras.")
    esperar(1)

    decisao = encerrar_missao()
    if (decisao):
      break