from ..interface import loading, menu
from ..utils import encerrar_missao, esperar, limpar

mensagens = {
  "A": "Parabéns, você tirou A!",
  "B": "Muito bem, você tirou B.",
  "C": "Bom trabalho, você tirou C.",
  "D": "Fique atento, você tirou D.",
  "F": "Estude um pouco mais, você tirou F."
}

def verificar_nota(nota):
  if (nota > 100):
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
  menu("Missão 3: Recuperando o Sistema de Notas")

  while True:
    limpar()
    nota_aluno = int(input("Informe sua nota: "))

    if not isinstance(nota_aluno, int):
      print("Informe um número válido")
      esperar(2)
      continue

    loading("Calculando nota")

    resultado = verificar_nota(nota_aluno)
    print(resultado.title())
    esperar(1)

    decisao = encerrar_missao()
    if (decisao):
      break