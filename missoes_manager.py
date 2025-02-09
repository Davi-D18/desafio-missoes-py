from missoes.m1.m1 import executar_m1
from missoes.m2.m2 import executar_m2
from missoes.m3.m3 import executar_m3
from missoes.m4.m4 import executar_m4
from missoes.m5.m5 import executar_m5
from missoes.m6.m6 import executar_m6
from missoes.m7.m7 import executar_m7
from missoes.m8.m8 import executar_m8
from missoes.m9.m9 import executar_m9
from missoes.m10.m10 import executar_m10
from missoes.utils import esperar, limpar

missoes = {
    "1": executar_m1,
    "2": executar_m2,
    "3": executar_m3,
    "4": executar_m4,
    "5": executar_m5,
    "6": executar_m6,
    "7": executar_m7,
    "8": executar_m8,
    "9": executar_m9,
    "10": executar_m10
}

def listar_missoes():
    """Exibe a lista de missões disponíveis."""
    print("\nEscolha uma missão para executar:")
    for chave in missoes:
        print(f"{chave} - Missão {chave}")

def executar_missao(escolha):
    """Executa a missão escolhida."""
    if escolha in missoes:
        limpar()
        missoes[escolha]()  # Chama a função correspondente
    else:
        print("Missão inválida. Tente novamente.")
        esperar(2)
