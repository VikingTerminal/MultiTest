import requests
import time
import os
import socket
import string
import datetime
import random
from googletrans import Translator
from bs4 import BeautifulSoup

MAX_ATTEMPTS = 3  # Maximum number of attempts

def get_ip_domain_info():
    ip = input("\033[1;36mEnter the IP address or domain: \033[0m")
    try:
        host_info = socket.gethostbyname(ip)
        print(f"\033[1;32mThe IP address of {ip} is: {host_info}\033[0m")
    except socket.error as e:
        print(f"\033[1;31mError while retrieving the IP address: {e}\033[0m")

def scan_ports():
    ip = input("\033[1;36mEnter the IP address to scan: \033[0m")
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"\033[1;32mPort {port} is open\033[0m")
            sock.close()
    except socket.error as e:
        print(f"\033[1;31mError while scanning ports: {e}\033[0m")

def send_ping():
    destination = input("\033[1;36mEnter the IP address or domain for ping: \033[0m")
    ping_quantity = input("\033[1;36mEnter the quantity of pings: \033[0m")
    ping_speed = input("\033[1;36mEnter the ping speed (in milliseconds): \033[0m")

    try:
        os.system(f"ping -c {ping_quantity} -i {ping_speed} {destination}")
    except Exception as e:
        print(f"\033[1;31mError while sending pings: {e}\033[0m")

def send_syn_ack():
    destination = input("\033[1;36mEnter the IP address or domain to send SYN/ACK: \033[0m")
    port = int(input("\033[1;36mEnter the port number: \033[0m"))
    syn_ack_quantity = int(input("\033[1;36mEnter the quantity of SYN/ACK: \033[0m"))
    syn_ack_speed = float(input("\033[1;36mEnter the SYN/ACK sending speed (in seconds): \033[0m"))

    try:
        for _ in range(syn_ack_quantity):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((destination, port))
            print("\033[1;32mSYN/ACK successfully sent\033[0m")
            time.sleep(syn_ack_speed)
    except Exception as e:
        print(f"\033[1;31mError while sending SYN/ACK: {e}\033[0m")
    finally:
        sock.close()

def generate_password():
    length = int(input("\033[1;36mEnter the password length: \033[0m"))
    alphanumeric = input("\033[1;36mDo you want the password to be alphanumeric? (yes/no): \033[0m").lower() == 'yes'
    with_symbols = input("\033[1;36mDo you want the password to contain symbols? (yes/no): \033[0m").lower() == 'yes'
    password_quantity = int(input("\033[1;36mEnter the number of passwords to generate: \033[0m"))

    characters = string.ascii_letters + string.digits
    if with_symbols:
        characters += string.punctuation

    for _ in range(password_quantity):
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"\033[1;32mGenerated Password: {password}\033[0m")

    save_file = input("\033[1;36mDo you want to save the passwords to a file? (yes/no): \033[0m").lower()
    if save_file == 'yes':
        file_name = input("\033[1;36mEnter the file name (with extension): \033[0m")
        with open(file_name, 'w') as file:
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
⠀⠀⢠⣿⣿⣿⣿⣟⡀⢀⣿⣿⣿⣿⣷⡈⢉⣉⣉⣉⣁⣀⣀⣻⣿⣿⣿⡄⠀⠀
⠀⣠⣿⣿⣿⣿⣿⡟⢠⣿⣿⣿⣿⡟⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀
⢰⣿⣿⣿⣿⣿⠟⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀
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

    # In your main while loop
    while True:
        print("\033[1;34mChoose an option:")
        print("1. IP/Domain Info")
        print("2. Scan Domain Ports")
        print("3. Send Ping [advanced]")
        print("4. Test DDoS SYN/ACK")
        print("5. Generate Password")
        print("6. Exit\033[0m")

        choice = input("\033[1;36mEnter the number of the desired option (1/2/3/4/5/6): \033[0m")

        if choice == "1":
            get_ip_domain_info()
        elif choice == "2":
            scan_ports()
        elif choice == "3":
            send_ping()
        elif choice == "4":
            send_syn_ack()
        elif choice == "5":
            generate_password()
        elif choice == "6":
            print("\033[1;33mThank you for using the program!.. For feedback and suggestions, you can contact me on Telegram at t.me/vikingterminal \033[0m")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")
