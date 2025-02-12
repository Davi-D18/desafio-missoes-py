from .esperar import esperar
from .limpar_terminal import limpar


def encerrar_missao():
  print("")
  limpar()
  decisao = input("Deseja encerrar esta missão? (s/n) ").strip().lower()
      
  if decisao == "s":
    print("Saindo da missão...")
    esperar(1)
    return True
  elif decisao == "n":
    return False
  else:
    print("Opção inválida, tente novamente.")
    esperar(1)
    return encerrar_missao()