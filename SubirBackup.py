import pyautogui as pa
import time
import keyboard
import os
import threading
import pyperclip


#intervalo entre os comandos
pa.PAUSE = 1


#Para poder interromper o código
interromper = False
def monitorar_interrupcao():
    global interromper
    keyboard.wait('esc')
    interromper = True
    print("Interrupção solicitada pelo usuário. Finalizando...")

#função principal/inicial
def main():
    global MAC
    print('-----Bem Vindo ao Automatizador VPU-----')
    MAC = input('por gentileza digite o mac: ')
    print('o mac é:', MAC)
    verificar()

#Verificação
def verificar():
    while not interromper:
        print('1-Roteador Novo da Caixa')
        print('2-Roteador da Rua')
        try:
            veri = int(input('digite uma opção: '))
            if veri == 1:
                print('aguarde alguns instantes')
                Acesso()
                RoteadorF()
                break
            
            elif veri == 2:
                print('aguarde alguns instantes')
                Acesso()
                RoteadorRua()
                break
            
            else:
                print ('opção inválida')
            
        except ValueError: 
            os.system('cls')
            print('Entrada inválida. Digite apenas números.')
            print('digite enter para continuar')
            keyboard.wait('enter')
        if interromper:
            break

#acessa o navegador
def Acesso():
    if interromper:
        return
    pa.press('Win')
    pa.write('edge')
    pa.press('enter')
    pa.sleep(1)

#acessa o roteador caso seja de fábrica
def RoteadorF():  
    if interromper:
        return  
    pa.write('192.168.1.1')
    pa.press('enter')
    pa.write('multipro')
    pa.press('tab')
    pa.write('multipro')
    pa.press('enter')
    novo()

def RoteadorRua():
    if interromper:
        return
    pa.write('192.168.1.1')
    pa.press('enter')
    pa.write('multipro')
    pa.press('tab')
    pa.write('Vpu@2018')
    pa.press('enter')
    gerenciamento()

#remove o assistente
def novo():
    if interromper:
        return
    pa.press('tab', 6)
    pa.press('enter')
    gerenciamento()

#acessa o gerenciamento 
def gerenciamento():
    if interromper:
        return
    pa.press('enter')
    pa.press('tab', 5)
    pa.press('enter')
    pa.press('tab', 9)
    pa.press('enter')
    pa.press('F11')
    pa.click(x=1831, y=181)
    pa.mouseDown(button='left')
    time.sleep(1)
    pa.mouseUp(button='left')
    pa.click(x=1646, y=186)
    backup()

#acessa o backup
def backup():
    if interromper:
        return
    pa.click(x=1069, y=522)
    pa.press('tab')
    pa.press('enter')
    pa.write('C:\\Users\\nocvp\\OneDrive\Documentos\\Vem-pra-Uno-ZTE-H199A-main')
    pa.press('enter')
    pa.write('default.bin')
    pa.press('enter')
    Cbackup()

#confirma o backup
def Cbackup():
    if interromper:
        return
    pa.press('tab')
    pa.press('enter')
    pa.press('tab')
    pa.press('enter')
    time.sleep(70)
    logar()
    
def logar():
    if interromper:
        return
    pa.write('multipro')
    pa.press('tab')
    pa.write('Vpu@2018')
    pa.press('enter')
    pa.press('tab', 5)
    pa.press('enter')
    wan()

#acessa a Wan e altera o ppoe
def wan():
    if interromper:
        return
    pa.press('tab', 3)
    pa.press('enter')
    pa.press('tab', 7)
    pa.press('enter')
    pa.click(x=1022, y=388)
    pa.press('tab', 6)
    pa.write(MAC[-6:] + '@vemprauno')
    lan()

#acessa o wifi e senha
def lan():
    if interromper:
        return
    pa.press('tab', 11)
    pa.press('enter')
    time.sleep(1)
    pa.press('tab', 7, 1)
    pa.press('enter')
    pa.press('tab', 7)
    pa.press('enter')
    pa.click(x=1115, y=652)
    pa.press('tab', 3)
    g4()

#usuario e senha do 4g
def g4():
    pa.write('VempraUno_' + MAC[-4:])
    pa.press
    pa.press('tab', 3)
    pa.write(MAC[-8:])
    pa.press('tab', 4)
    pa.press('enter')
    pa.press('tab')
    pa.press('enter')

if __name__ == "__main__":
    # Inicia o monitoramento da tecla de interrupção em uma thread separada
    interrupcao_thread = threading.Thread(target=monitorar_interrupcao)
    interrupcao_thread.daemon = True
    interrupcao_thread.start()
    
    main()