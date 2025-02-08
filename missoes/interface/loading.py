import sys
import time


def loading(mensagem="Carregando", tempo=3):
    """
    Exibe uma animação de loading no terminal com uma barra girando.

    :param mensagem: Texto exibido antes da animação (padrão: "Carregando")
    :param tempo: Tempo total da animação em segundos (padrão: 3s)
    """
    simbolos = ["\\", "|", "/", "-"]
    
    print(mensagem, end=" ", flush=True)
    
    for i in range(tempo * 4):  # Multiplica por 4 porque há 4 símbolos no loop
        sys.stdout.write(f"\r{mensagem} {simbolos[i % 4]}   ")
        sys.stdout.flush()
        time.sleep(0.25)  # Tempo entre cada mudança

    # Limpa a linha anterior antes de exibir "Concluído"
    sys.stdout.write("\r" + " " * (len(mensagem) + 5) + "\r")  
    print("✅ Concluído!")