from asyncio import protocols
from colorama import Fore, init
import socket
import random


port = 0
valid_proxy = []
form = ""
proxy = ""

arquivo = str(input("Proxy archive name: "))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
init(convert=True)

while True:
    try:
        with open(f"{arquivo}", "r") as reg:
            for proxys in reg.readlines():
                divisor = proxys.split(":")
                proxy = divisor[0]
                if "\n" in divisor[1]:
                    divisor[1].replace("\n", "")
                port = int(divisor[1])
                
                try:
                    client.connect(proxy, port)
                    print(f"{Fore.GREEN}{proxy}:{port} ==> Válida{Fore.RESET}")
                    with open(f"valid_proxies{random.randint(0, 1000)}.txt", "a+") as vali:
                        vali.write(f"{proxy}:{port}")

                    valid_proxy.append(form)
                except:
                    print(f"{Fore.RED}{proxy}:{port} ==> Inválida{Fore.RESET}")

                client.close()
            break
    except FileNotFoundError:
        print(f"{Fore.RED}Nome inválido{Fore.RESET}")
        break

if valid_proxy != []:
    for valids in valid_proxy:
        print(f"{Fore.GREEN}{valids}{Fore.RESET}")
else:
    print(f"{Fore.RED}Nenhuma proxy encontrada{Fore.RESET}")
            

                

        
    