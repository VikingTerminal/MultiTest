import requests
import time
import os
import socket
import string
import datetime
import random
from googletrans import Translator
from bs4 import BeautifulSoup

MAX_TENTATIVI = 3  # Numero massimo di tentativi

def info_ip_domino():
    ip = input("\033[1;36mInserisci l'indirizzo IP o il dominio: \033[0m")
    try:
        host_info = socket.gethostbyname(ip)
        print(f"\033[1;32mL'indirizzo IP di {ip} è: {host_info}\033[0m")
    except socket.error as e:
        print(f"\033[1;31mErrore durante la ricerca dell'indirizzo IP: {e}\033[0m")

def scan_porte():
    ip = input("\033[1;36mInserisci l'indirizzo IP da scannerizzare: \033[0m")
    try:
        for porta in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            
            result = sock.connect_ex((ip, porta))
            
            if result == 0:
                print(f"\033[1;32mPorta {porta} aperta\033[0m")
            sock.close()
    except socket.error as e:
        print(f"\033[1;31mErrore durante la scansione delle porte: {e}\033[0m")

def invia_ping():
    destinazione = input("\033[1;36mInserisci l'indirizzo IP o il dominio per il ping: \033[0m")
    quantita_ping = input("\033[1;36mInserisci la quantità di ping: \033[0m")
    velocita_ping = input("\033[1;36mInserisci la velocità dei ping (in millisecondi): \033[0m")

    try:
        os.system(f"ping -c {quantita_ping} -i {velocita_ping} {destinazione}")
    except Exception as e:
        print(f"\033[1;31mErrore durante l'invio dei ping: {e}\033[0m")

def invia_syn_ack():
    destinazione = input("\033[1;36mInserisci l'indirizzo IP o il dominio per inviare SYN/ACK: \033[0m")
    porta = int(input("\033[1;36mInserisci il numero di porta: \033[0m"))
    quantita_syn_ack = int(input("\033[1;36mInserisci la quantità di SYN/ACK: \033[0m"))
    velocita_syn_ack = float(input("\033[1;36mInserisci la velocità di invio SYN/ACK (in secondi): \033[0m"))

    try:
        for _ in range(quantita_syn_ack):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((destinazione, porta))
            print("\033[1;32mSYN/ACK inviato con successo\033[0m")
            time.sleep(velocita_syn_ack)
    except Exception as e:
        print(f"\033[1;31mErrore durante l'invio di SYN/ACK: {e}\033[0m")
    finally:
        sock.close()

def genera_password():
    lunghezza = int(input("\033[1;36mInserisci la lunghezza della password: \033[0m"))
    alfanumerica = input("\033[1;36mVuoi che la password sia alfanumerica? (sì/no): \033[0m").lower() == 'sì'
    con_simboli = input("\033[1;36mVuoi che la password contenga simboli? (sì/no): \033[0m").lower() == 'sì'
    quantita_password = int(input("\033[1;36mInserisci il numero di password da generare: \033[0m"))

    caratteri = string.ascii_letters + string.digits
    if con_simboli:
        caratteri += string.punctuation

    for _ in range(quantita_password):
        password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
        print(f"\033[1;32mPassword generata: {password}\033[0m")

    salva_file = input("\033[1;36mVuoi salvare le password in un file? (sì/no): \033[0m").lower()
    if salva_file == 'sì':
        nome_file = input("\033[1;36mInserisci il nome del file (con estensione): \033[0m")
        with open(nome_file, 'w') as file:
            for password in passwords:
                file.write(password + '\n')

def display_animation():
    animations = [ """\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⡀⠀⠀⠀⠀⢀⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⡄⠀⠀⢀⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⡄⠠⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣆⠹⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠛⣿⣿⣿⣿⣦⠙⠟⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣿⣿⣿⡿⠁⠀⠘⣿⣿⣿⣿⣧⠀⠈⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣿⡟⠁⢀⣾⣷⡈⢿⣿⣿⣿⣷⡀⠈⢻⣿⣿⣿⣷⡀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣟⡀⢀⣾⣿⣿⣷⡈⢉⣉⣉⣉⣁⣀⣀⣻⣿⣿⣿⣿⡄⠀⠀
⠀⣠⣿⣿⣿⣿⣿⡟⢠⣿⣿⣿⣿⡟⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀
⢰⣿⣿⣿⣿⣿⠟⣠⣿⣿⣿⣿⠟⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣏⣀⣀⣀⣀⣀⣀⣰⣶⣶⣶⣶⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀
 _ _  _  _    _           
| | |<_>| |__<_>._ _  ___ 
| ' || || / /| || ' |/ . |
|__/ |_||_\_\|_||_|_|\_. |
t.me/VikingTerminal  <___'
        """
    ]

    for frame in animations:
        print(frame)
        time.sleep(1)


if __name__ == "__main__":
    display_animation()

    # Nel tuo loop while principale
    while True:
        print("\033[1;34mScegli un'opzione:")
        print("1. Info IP/Dominio")
        print("2. Scan Porte dominio")
        print("3. Invia Ping [avanzato]")
        print("4. Test DDoS SYN/ACK")
        print("5. Genera password")
        print("6. Esci\033[0m")

        scelta = input("\033[1;36mInserisci il numero dell'opzione desiderata (1/2/3/4/5/6): \033[0m")

        if scelta == "1":
            info_ip_domino()
        elif scelta == "2":
            scan_porte()
        elif scelta == "3":
            invia_ping()
        elif scelta == "4":
            invia_syn_ack()
        elif scelta == "5":
            genera_password()
        elif scelta == "6":
            print("\033[1;33mGrazie per utilizzare il programma!.. Per segnalazioni e consigli puoi contattarmi su telegram scrivendo a t.me/vikingterminal \033[0m")
            break
        else:
            print("Scelta non valida. Inserisci un numero tra 1 e 6.")
