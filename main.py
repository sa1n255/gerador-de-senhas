from functions.functions import *
from functions import exceptions
from functions.colors import *

import sys

def main(): 
    show_banner()

    try: 
        user_password_length = int(input("Tamanho da senha: (Recomendado: 8 até 50)\n>>> "))

        while user_password_length <= 2:
            print(vermelho + "Só é possivel gerar senhas com no minimo 3 indices de tamanho" + reset)
            user_password_length = int(input("Tamanho da senha: (Recomendado: 8 até 50)\n>>> "))

        if user_password_length <= 7: 
            print(amarelo + "Aviso: Sua senha é menor que 8 indices." + reset)
            c = confirm()
            if not c:
                print(vermelho + "Encerrando..." + reset)
                sys.exit(1)

    except KeyboardInterrupt as ki: 
        exceptions.keyboard_interrupt(ki)

    except Exception as error: 
        exceptions.exception(error)
    
    else: 
        print("Gerando senha...")

    print(f"Senha gerada: {bold + password_generator(user_password_length) + reset}")

if __name__ == '__main__':
    version_check()
    main()
