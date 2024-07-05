import pyautogui as pa
import time
import keyboard
import os
import threading
import pyperclip
import requests

# Configurações do roteador
router_ip = '192.168.1.1'  # Endereço IP do roteador
username = 'multipro'         # Nome de usuário do roteador
password = 'Vpu@2018'         # Senha do roteador

# URL de login do roteador (essa URL é um exemplo e pode precisar ser ajustada)
login_url = f'http://{router_ip}'

# Dados de login (ajuste os parâmetros conforme necessário)
login_data = {
    'UserName': username,
    'PassWord': password,
    'action': 'login'
}

# Iniciar uma sessão para manter o estado de login
session = requests.Session()

# Enviar requisição de login
response = session.post(login_url, data=login_data)

# Verificar se o login foi bem-sucedido
if response.status_code == 200:
    print("Login bem-sucedido!")
    
    # URL da página de informações do roteador (essa URL é um exemplo e pode precisar ser ajustada)
    info_url = f'http://{router_ip}'
    
    # Obter informações do roteador
    response = session.get(info_url)
    
    if response.status_code == 200:
        # Imprimir conteúdo da página de informações (provavelmente em HTML)
        print(response.text)
    else:
        print("Falha ao obter informações do roteador.")
else:
    print("Falha no login.")

time.sleep(50)