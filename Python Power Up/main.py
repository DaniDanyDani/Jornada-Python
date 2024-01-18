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
    
    Passo 3: Com o pyautogui abrir o chrome e fazer login no "servidor"
        Pyautogui.press – Serve para pressionar uma teclado seu teclado
        Pyautogui.write – Serve para escrever com o teclado (como se fosse você digitando)
        Pyautogui.click – Serve para clicar com o mouse
        Pyautogui.scroll – Serve para usar o "scroll" do mouse
        Pyautogui.position() – Serve para pegar a posição em que o mouse se encontra

    passo 4: Cadastrar produto por produto


'''

import pandas as pd
import pyautogui
import time

tabela = pd.read_csv("produtos.csv")
print(tabela)