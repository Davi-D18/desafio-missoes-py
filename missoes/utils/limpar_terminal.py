import os


def limpar():
    """Limpa o terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
