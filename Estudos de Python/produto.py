#Passo 1 - Entrar no Sistema da Empresa
#link: 
#Passo 2 - Criar o Login
#Passo 3 - Pegar/Importar a base de dados
#Passo 4 - Cadastrar um produto
#Passo 5 - Repitir o passo 4 até cadastrar todos os produtos

# Transformando esse passo a passo em Python

#comandos do pyautogui
import pyautogui # Ferramenta do mouse que automotiza o mouse, teclado e a tela do seu computador
#pyautogui.click - clicar com o mouse
#pyautogui.write - escrever um texto
#pyautogui.pree - apertar uma tecla
#pyautogui.hotkey - combinação de teclas
#pyautogui.scroll - rolar a tela para cima ou para baixo

import time # Controla o tempo

#COMANDO PARA INSTALAR O PANDAS
#pip install pandas openpyx1.numpy

pyautogui.PAUSE = 0.5

# passo 1 - entrar no sistema
# abrir o navegador
pyautogui.press('win')
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link: https://dip.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write(" https://dip.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)


# Passo 2 - Fazer o Login
print(pyautogui.position(x=830, y=464))
pyautogui.hotkey("ctrl","a")
pyautogui.write("jujubaatomica508@gmail.com")

# passar para o campo a senha
pyautogui.press("tab")
pyautogui.write("minha senha")

pyautogui.click(x=941, y=669)

time.sleep(3)

# Passo 3 - Importar a base de dados
import pandas


tabelas = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 - Cadastrar o produto
#para cada linha da minha tabelas
for linha in tabela.index: 

#codigo
pyautogui.click(x=656, y=337)

#tabela.loc[linha,coluna]
tabela.loc[5,"codigo"]

codigo = str(tabela.loc[linha, "codigo"])
pyautogui.write("codigo")

#marca
pyautogui.press("tab")
marca= str(tabela.loc[linha, "marca"])
pyautogui.write(marca)

#tipo
pyautogui.press("tab")
tipo = str(tabela.loc[linha, "tipo"])
pyautogui.write(tipo)

#categoria
pyautogui.press("tab")
categoria = str(tabela.loc[linha, "categoria"])
pyautogui.write(categoria)

#preco_unitario
pyautogui.press("tab")
preco_unitario = str(tabela.loc[linha, "preco_unitario"])
pyautogui.write(preco_unitario)

#custo
pyautogui.press("tab")
custo = str(tabela.loc[linha, "custo"])
pyautogui.write(custo)

#obs
pyautogui.press("tab")
obs = str(tabela.loc[linha, "obs"])
if obs ! = "nan"
pyautogui.write(obs)


pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.scroll(5000)