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

global multipro
global Vpu
multipro = ('multipro')
Vpu = ('Vpu@2018')

#função principal/inicial
def main():
    global MAC
    global MACgrande
    global MACpequeno
    print('-----Bem Vindo ao Automatizador VPU-----')
    MAC = input('por gentileza digite o mac: ')
    MACgrande = MAC.upper()
    MACpequeno = MAC.lower()
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
    pa.write(multipro)
    pa.press('tab')
    pa.write(multipro)
    pa.press('enter')
    novo()

#Acessa o roteador caso seja da rua
def RoteadorRua():
    if interromper:
        return
    pa.write('192.168.1.1')
    pa.press('enter')
    pa.write(multipro)
    pa.press('tab')
    pa.write(Vpu)
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
    pa.press('tab', 5,)
    pa.press('enter')
    pa.press('tab', 9)
    pa.press('enter')
    pa.press('F11')
    pa.click(x=977, y=146)
    pa.mouseDown(button='left')
    time.sleep(1)
    pa.mouseUp(button='left')
    pa.click(x=859, y=149)
    backup()

#acessa o backup
def backup():
    if interromper:
        return
    pa.click(x=333, y=460)
    pa.press('tab')
    pa.press('enter')
    pa.write('C:\\Users\\noc autum\\Documents\\Vem-pra-Uno-ZTE-H199A-main')
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
    time.sleep(60)
    fecharjanela()

#Fecha a janela para impedir o bug de login do H199A
def fecharjanela():
    if interromper:
        return
    pa.keyDown('alt')
    pa.press('f4')
    pa.keyUp('alt')
    Acesso()
    logar()
    
#Para poder logar no roteador pós backup
def logar():
    if interromper:
        return
    pa.write('192.168.1.1')
    pa.press('enter')
    pa.sleep(5)
    pa.press('f11')
    pa.press('f5')
    pa.write(multipro)
    pa.press('tab')
    pa.write(Vpu)
    pa.press('tab')
    pa.press('enter')
    removassistente()

def removassistente():
    pa.press('tab', 6)
    pa.press('enter')
    wlan()

#acessa a Wlan e altera o ppoe
def wlan():
    if interromper:
        return
    vemprauno = ('@vemprauno')
    pa.press('tab', 3)
    pa.press('enter')
    pa.press('tab', 7, 1)
    pa.press('enter')
    pa.click(x=343, y=333)
    pa.press('tab', 6)
    pa.write(MACgrande[-6:] + vemprauno)
    pa.press('tab', 11, 0.5)
    pa.press('enter')
    lan()

#acessa o wifi e senha
def lan():
    if interromper:
        return
    time.sleep(1)
    pa.press('home')
    pa.click(x=695, y=90)
    pa.press('tab', 7)
    pa.press('enter')
    pa.click(x=348, y=551)
    pa.press('tab', 3)
    g4()

#usuario e senha do 4g
def g4():
    vemprauno = ('VempraUno_')
    pa.write(vemprauno + MACgrande[-4:])
    pa.press('tab', 3)
    pa.write(MACpequeno[-8:])
    pa.press('tab', 4)
    pa.press('enter')
    pa.press('tab')
    pa.press('enter')
    relatorio()

def relatorio():
    os.system('cls')
    vemprauno = ('@vemprauno')
    Vemprauno = ('VempraUno_')
    print ('o ppoe é: ' + MACgrande[-6:] + vemprauno)
    
    print ('o usuario é: '+ Vemprauno + MACgrande[-4:])
    print ('a senha é: ' + MACpequeno[-8:])
    time.sleep (60)
    

if __name__ == "__main__":
    # Inicia o monitoramento da tecla de interrupção em uma thread separada
    interrupcao_thread = threading.Thread(target=monitorar_interrupcao)
    interrupcao_thread.daemon = True
    interrupcao_thread.start()
    
    main()