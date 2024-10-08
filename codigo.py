#imports pro Python
import pyautogui
import time
import pandas

#passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho no teclado (ctrl + c)
# pyautogui.PAUSE = 1 -> serve para pausar por 1 segundo por exemplo
# pandas.read -> lê algum arquivo que vc tenha de base de dados

# fazendo ele andar mais devagar nas instruções para dar tempo de rodar
pyautogui.PAUSE = 0.5

# Para entrar no edge:
# apertar a tecla windows
pyautogui.press("win")

# digitar o edge e entrar nele
pyautogui.write("edge")
pyautogui.press("enter")

# digitar o link e entrar nele
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# quero dar uma pausa de 3s
time.sleep(3)

# passo 2: fazer login

# clicar com o mouse na aba do gmail
# usar o arquivo 'auxiliar' para achar
pyautogui.click(x=737, y=433)

# escrever email
pyautogui.write("pythonautomacao@gmail.com")

# passar pra senha
pyautogui.press("tab")

# escrever a senha
pyautogui.write("minhasenha")

# passar pra logar
pyautogui.press("tab")

# entrar clicando em logar
pyautogui.press("enter")

# passo 3: importar base de dados
# pip install pandas -> é usado para importar dados

tabela = pandas.read_csv("produtos.csv")
print (tabela)

# passo 4: cadastrar 1 produto

# clicando no primeiro campo
pyautogui.click(x=741, y=294)

linha = 0

# executar para cada linha na tabela
for linha in tabela.index:

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # clicar em enviar
    pyautogui.press("enter")
    pyautogui.scroll(1000)

    # passo 5: repetir o cadastro ate acabar os produtos

    # somando na linha para ir pro proximo item
    linha = linha + 1
    # clicando no primeiro campo
    pyautogui.click(x=741, y=294)