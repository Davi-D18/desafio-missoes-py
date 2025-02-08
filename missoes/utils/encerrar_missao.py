from .esperar import esperar


def encerrar_missao():
  print("")
  decisao = input("Deseja encerrar esta missão? (s/n) ").strip().lower()
      
  if decisao != "n":
    print("Saindo da missão...")
    esperar(1)
    return True
  else:
    return False