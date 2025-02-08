import time


def menu(titulo, descricao="", tempo=2):
    # Define um padding para garantir espaço extra e calcula a largura mínima
    padding = 4
    largura = max(50, len(titulo) + padding, len(descricao) + padding)
    borda = "=" * largura

    print(borda)
    print(titulo.center(largura).title())
    if descricao:
        print("-" * largura)
        print(descricao.center(largura).title())
    print(borda)

    time.sleep(tempo)
