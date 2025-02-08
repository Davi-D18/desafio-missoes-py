from ..interface import loading, menu
from ..utils import encerrar_missao, esperar, limpar


def verificar_idade(idade):
  if (idade >= 18 and idade <= 65):
    print("Você deve votar obrigatoriamente")
  elif (idade >= 16 and idade <= 17 or idade > 65):
    print("Você pode votar, mas é opcional")
  else:
    print("Você não tem permissão para votar ainda")
    esperar(2)

def executar_m2():
  menu("Missão 2: O Sistema Eleitoral Secreto 📝",
       "Verifica se um usuário pode votar.", 3)

  while True:
      limpar()
      idade_usuario = int(input("Informe sua idade: "))
      loading("Verificando sua idade", 2)

      verificar_idade(idade_usuario)
      
      decisao = encerrar_missao()

      if (decisao):
        break    