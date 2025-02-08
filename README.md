# 🚀 Desafio Vai na Web - Resgate do Sistema

Bem-vindo(a)! Esse é o Desafio 1 do Módulo de **Back-end** no curso Full-Stack do Vai na Web

## 📌 Sobre o Repositório
Este projeto consiste em uma série de desafios programáticos que simulam a recuperação de um sistema comprometido por um vírus. O objetivo é reforçar conceitos fundamentais de programação, como estrutura condicional, loops e listas.

Cada missão é referente a uma atividade

## 🏆 Missões

### 🔹 Missão 1: Restaurando as Regras Escolares 📝
**Objetivo:** Criar um programa que verifique se um aluno foi aprovado (nota ≥ 6) ou reprovado (nota ≤ 5).

### 🔹 Missão 2: O Sistema Eleitoral Secreto 📝
**Objetivo:** Criar um programa que pergunte a idade do usuário e informe se ele pode votar (idade mínima: 16 anos).

### 🔹 Missão 3: Recuperando o Sistema de Notas 📊
**Objetivo:** Criar um programa que peça a nota do aluno e exiba sua classificação com base na escala de A a F.

### 🔹 Missão 4: Restaurando a Identificação de Números ⚖️
**Objetivo:** Criar um programa que solicite dois números e exiba a soma deles.

### 🔹 Missão 5: Recuperando o Cofre de Segurança 🔒
**Objetivo:** Criar um programa que valide se a senha informada pelo usuário é "Python123".

### 🔹 Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
**Objetivo:** Exibir os números de 1 a 10 utilizando um loop **while**.

### 🔹 Missão 7: Organizando a Lista 📋
**Objetivo:** Criar uma lista com os números [8, 3, 10, 1, 5] e exibi-los em ordem crescente.

### 🔹 Missão 8: Acessando os Registros de Alunos 🏷️
**Objetivo:** Criar uma tupla com os nomes ["Ana", "Bruno", "Carla", "Daniel", "Eduardo"] e exibir o primeiro e o último nome.

### 🔹 Missão 9: Calculando o Dobro de um Número 🛠️
**Objetivo:** Criar uma função que receba um número e retorne o dobro do seu valor.

### 🔹 Missão 10: Contando Letras 🔄
**Objetivo:** Criar uma função que receba um nome e retorne a quantidade de letras desse nome.


## 📂 Estrutura de Pastas
O projeto está organizado da seguinte forma:

```
├── docs/                
│   ├── missoes.md       # Descrição detalhada das missões
│
├── missoes/             # Pasta principal contendo as missões e utilitários
│   ├── interface/       # Funções para algum tipo de "interface"
│   │   ├── __init__.py
│   │   ├── menu.py      # Exibe um menu no terminal
│   │   ├── loading.py   # Simula um loading durante a execução
│   │
│   ├── m1/ - m10/        # Módulos de cada missão
│   │   ├── m1.py - m10.py # Código das missões
│   │
│   ├── utils/           # Funções auxiliares para o programa
│   │   ├── __init__.py
│   │   ├── encerrar_missao.py   # Função para encerrar uma missão
│   │   ├── esperar.py           # Função para aguardar alguns segundos
│   │   ├── limpar_terminal.py   # Função para limpar o terminal
│
├── main.py              # Arquivo principal que gerencia o fluxo do programa
├── missoes_manager.py   # Gerenciador que executa as missões
```

### 📌 Detalhes dos Módulos
- **`interface/`**: Contém funções para interação visual no terminal, como menu e loading.
- **`utils/`**: Funções auxiliares para o funcionamento do programa, como limpar o terminal e aguardar alguns segundos.
- **`m1/ - m10/`**: Cada pasta representa uma missão específica, contendo sua implementação em um arquivo separado.
   - Obs: Algumas missões podem ter mais de 1 arquivo, é apenas para organização, separando funções
- **`missoes_manager.py`**: Arquivo responsável por executar as missões de acordo com a escolha do usuário.
- **`main.py`**: Arquivo principal que gerencia a interação do usuário com o sistema.
- **`__init__.py`**: O arquivo __init__.py indica ao Python que o diretório deve ser tratado como um pacote, facilitando importações

## 📚 Conceitos Utilizados
- Estruturas condicionais
- Loops
- Listas
- Funções

## 🛠 Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/Davi-D18/desafio-missoes-py.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd desafio-missoes-py
   ```
  
3. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

4. Execute o arquivo **`main.py`**:
   ```bash
   python3 main.py
   ```

Obs: execute o arquivo **`main.py`** para funcionar corretamente