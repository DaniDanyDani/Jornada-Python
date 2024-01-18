# A melhor forma de começar um programa é fazer um o passo a passo do mesmo

''' Passo a Passo:

    Passo 1: Instalar as bibliotecas externas
        pip install pyautogui
        pip install pandas

    Passo 2: Importar as bibliotecas e a base de dados "produtos.csv"
        import pandas as pd
        import pyautogui
        import time
        pd.read_csv("produtos.csv")

        tabela:
                 codigo       marca        tipo  categoria  preco_unitario  custo               obs
0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN
1    MOLO000192    Logitech       Mouse          2           19.95    5.0               NaN
2    CAHA000251     Hashtag      Camisa          1           25.00   11.0               NaN
3    CAHA000252     Hashtag      Camisa          2           25.00   11.0  Conferir estoque
4    MOMU000111  Multilaser       Mouse          1           11.99    3.4               NaN
..          ...         ...         ...        ...             ...    ...               ...
288  ACAP000192       Apple  Acessorios          2           19.00    3.8               NaN
289  ACSA0009.3     Samsung  Acessorios          3            9.55    2.1               NaN
290  CEMO000271    Motorola     Celular          1          279.00   72.5               NaN
291  FOMO000152    Motorola        Fone          2          150.00   33.0               NaN
292  CEMO000223    Motorola     Celular          3          229.00   55.0               NaN
    
    Passo 3: Com o pyautogui abrir o chrome e fazer login no "servidor"
        Pyautogui.press – Serve para pressionar uma teclado seu teclado
        Pyautogui.write – Serve para escrever com o teclado (como se fosse você digitando)
        Pyautogui.click – Serve para clicar com o mouse
        Pyautogui.scroll – Serve para usar o "scroll" do 
        
        criar um programa auxiliar (pegar_posicao.py) para adquirir as posições de onde iremos clicar como se fosse o mouse
        Pyautogui.position() – Serve para pegar a posição em que o mouse se encontra

    passo 4: Cadastrar produto por produto


'''

import pandas as pd
import pyautogui
import time

# É bom definir essas variáveis logo no início para que caso essas informações mudassem em um futuro simplesmente só mudar em um único ponto
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "emailqualquer@email.com"
senha = "senha_qualquer"

# Importando base de dados como "tabela"
tabela = pd.read_csv(r"C:\Users\Danie\OneDrive\Documentos\MeusProjetos\Jornada-Python\Python Power Up\produtos.csv")
# print(tabela) # Imprimir a tabela para saber como ela está formatada

pyautogui.PAUSE = 1 # dá um pause de 1 segundo a cada linha de código

pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter")

# agora dependendo do computador vai abrir ou não o crhome direto, no meu abre a seleção de perfis do chrome, então, irei pegar a posição em que o perfil que quero seja selecionado e então abrir o servidor

pyautogui.click(x=733, y=620)
pyautogui.write(link)
pyautogui.press("enter")

# já no site devemos selecionar a caixa de email para preencher os dados de entrada

pyautogui.click(x=689, y=513)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

# Já logado no servidor, devemos fazer os mesmos procedimentos para selecionar a primeira entrada

