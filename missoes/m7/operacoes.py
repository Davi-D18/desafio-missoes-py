lista = [8, 3, 10, 1, 5]


def escolher_operacao(operacao):
  match operacao:
    case 1:
      lista.sort()
      return lista
    case 2:
      lista.sort(reverse=True)
      return lista
    case _:
      print("Opção inválida, tente novamente")
