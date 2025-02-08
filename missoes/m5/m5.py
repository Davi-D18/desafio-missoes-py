from ..interface import loading, menu
from ..utils import encerrar_missao, esperar, limpar
from .functions import verificar_senha


def executar_m5():
  menu("Missão 5: Recuperando o Cofre de Segurança 🔒", "valida uma senha se está certa ou não.")

  while True:
    limpar()
    usuario = input("Informe seu nome: ").title()
    tentativa_senha = input("Informe a senha para acessar o sistema: ")
    loading("Verificando senha, aguarde")

    verificar_senha(tentativa_senha, usuario)
    esperar(2)
    decisao = encerrar_missao()

    if(decisao):
      break

