from ..interface import loading, menu
from ..utils import encerrar_missao, esperar, limpar

Error = False

def verificar_aprovacao(nota):
  global Error

  if (nota > 10):
    Error = True
    return "A nota deve ser entre 0 e 10, tente novamente"
  elif (nota >= 6):
    return "Parabéns você está aprovado :)"
  else:
    return "Infelizmente você não está aprovado :("


def executar_m1():
    global Error
    menu("Missão 1: Restaurando as Regras Escolares",
         "Verifica se um aluno foi aprovado ou não.", 3)
    
    while True:
      limpar()
      nota = int(input("Digite sua nota entre 0 e 10: "))

      loading("Aguarde enquanto o resultado é processado", 2)

      print(verificar_aprovacao(nota))
      esperar(2)

      if (Error):
        Error = False
        continue

      decisao = encerrar_missao()

      if (decisao):
        break


      
            