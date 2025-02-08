from ..interface import loading, menu
from ..utils import encerrar_missao, esperar, limpar

Error = False

mensagens = {
  "A": "Parabéns, você tirou A!",
  "B": "Muito bem, você tirou B.",
  "C": "Bom trabalho, você tirou C.",
  "D": "Fique atento, você tirou D.",
  "F": "Estude um pouco mais, você tirou F."
}

def verificar_nota(nota):
  global Error

  if (nota > 100):
    Error = True
    return "Nota inválida, tente novamente"
  elif (nota >= 90 and nota <= 100):
    return mensagens["A"]
  elif (nota >= 80 and nota <= 89):
    return mensagens["B"]
  elif (nota >= 70 and nota <= 79):
    return mensagens["C"]
  elif(nota >= 60 and nota <= 69):
    return mensagens["D"]
  elif (nota < 60):
    return mensagens["F"]
  

def executar_m3():
  global Error
  menu("Missão 3: Recuperando o Sistema de Notas", "Classifica notas de alunos.")

  while True:
    limpar()

    try:
      nota_aluno = int(input("Informe sua nota entre 0 e 100: "))
    except ValueError:
      print("Informe um número válido")
      esperar(1)
      continue

    loading("Calculando nota")

    resultado = verificar_nota(nota_aluno)
    print(resultado.title())
    esperar(1)

    if (Error):
      Error = False
      continue

    decisao = encerrar_missao()
    if (decisao):
      break