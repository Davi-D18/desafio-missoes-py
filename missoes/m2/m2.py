from ..interface.loading import loading
from ..interface.menu import menu
from ..utils.encerrar_missao import encerrar_missao
from ..utils.esperar import esperar
from ..utils.limpar_terminal import limpar


def verificar_idade(idade):
  if (idade >= 16):
    print("Você pode votar")
  else:
    print("Você não tem permissão para votar ainda")
    esperar(2)

def executar_m2():
  menu("Missão 2: Sistema Eleitoral Secretos")

  while True:
      limpar()
      idade_usuario = int(input("Informe sua idade: "))
      loading("Verificando sua idade", 2)

      verificar_idade(idade_usuario)
      
      decisao = encerrar_missao()

      if (decisao):
        break    