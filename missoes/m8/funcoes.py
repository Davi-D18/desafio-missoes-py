from ..interface import loading
from ..utils import limpar

tupla_nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")

def exibir_nomes():
  loading("Consultando tupla", 1)
  print(f"Primeiro nome: {tupla_nomes[0]}")
  print(f"Último nome: {tupla_nomes[-1]}")

def adicionar_nomes():
  global tupla_nomes
  limpar()

  nome_adicionar = input("Qual nome deseja adicionar?: ").capitalize()

  loading("Adicionando", 1)

  lista_nomes = list(tupla_nomes)
  lista_nomes.append(nome_adicionar)
  tupla_nomes = tuple(lista_nomes)

  print(f"Sucesso! o nome {nome_adicionar} foi adicionado")
  print(tupla_nomes)
  return tupla_nomes