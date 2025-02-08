from missoes.interface.menu import menu
from missoes.utils.limpar_terminal import limpar
from missoes_manager import executar_missao, listar_missoes

menu("Bem-vindo ao Gerenciador de Missões!")

while True:
  limpar()
  listar_missoes()
  escolha = input("Digite o número da missão ou 'sair' para encerrar: ").strip()

  if escolha.lower() == "sair":
      print("Encerrando o programa...")
      break

  executar_missao(escolha)

