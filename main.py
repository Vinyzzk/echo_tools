import os
from modules.mlb import mlb_menu
from modules.check import check

def main_menu():
    print("""
 _____     _             _____           _     
|  ___|   | |           |_   _|         | |    
| |__  ___| |__   ___     | | ___   ___ | |___ 
|  __|/ __| '_ \ / _ \    | |/ _ \ / _ \| / __|
| |__| (__| | | | (_) |   | | (_) | (_) | \__ /
\____/\___|_| |_|\___/    \_/\___/ \___/|_|___/
                                       
""")
    print("--------------------")
    print("[1] Funcoes com MLB")
    print("[2] Gerador de links")
    print("[3] Tratamento de imagens")
    option = int(input("R: "))
    os.system('cls')
    if option == 1:
        mlb_menu()
    if option == 2:
        print("desenvolvimento...")
    if option == 3:
        print("desenvolvimento...")
        
    return option


if __name__ == "__main__":
    check()
    while True:
        option = main_menu()
        
        if option == 0:
            break