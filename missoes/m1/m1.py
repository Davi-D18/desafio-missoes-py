from ..interface.loading import loading
from ..interface.menu import menu
from ..utils.encerrar_missao import encerrar_missao
from ..utils.limpar_terminal import limpar


def verificar_aprovacao(nota):
  if (nota >= 6):
    return "Parabéns você está aprovado"
  else:
    return "Infelizmente você não está aprovado :("


def executar_m1():
    menu("Missão 1: Restaurando as Regras Escolares")
    
    while True:
      limpar()
      nota = int(input("Digite sua nota: "))

      loading("Aguarde enquanto o resultado é processado", 2)

      print(verificar_aprovacao(nota))

      decisao = encerrar_missao()

      if (decisao):
        break


      
            