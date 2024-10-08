import pyautogui
import time

# para identificar onde meu mouse ta, para achar os pixels na tela
# usando o time para demorar de executar e eu dar alt tab e por o mouse onde quero
time.sleep(5)
print(pyautogui.position())