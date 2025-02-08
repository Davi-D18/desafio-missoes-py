senha_de_acesso = "Python123"

def logado_sistema(nome):
  """Função para exibir quando o usuário estiver logado

  Args:
      nome (str): Nome do usuário
  """
  print(f"Seja bem vindo ao sistema {nome}")

def verificar_senha(senha, nome):
  """Função para verificar se a senha informada está certa

  Args:
      senha (str): Senha informado pelo usuário
      nome (str): Nome do usuário
  """
  global senha_de_acesso

  if(senha == senha_de_acesso):
    logado_sistema(nome)
  else:
    print("Senha incorreta")