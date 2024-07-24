import pyautogui
import time

# Caminho para a imagem que você capturou
imagem_alvo = 'nuvem.png'

# Loop até que a imagem seja encontrada
while True:
    try:
        # Tente localizar a imagem na tela
        posicao = pyautogui.locateOnScreen(imagem_alvo, confidence=0.8)
        
        # Se a imagem for encontrada, posicao não será None
        if posicao is not None:
            print("Imagem encontrada na tela!")
            break  # Sai do loop
        
    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada, tentando novamente...")

    # Aguarde um pouco antes de tentar novamente
    time.sleep(1)

print("O loop foi interrompido porque a imagem foi encontrada.")

