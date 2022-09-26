from functions.functions import *
from functions import exceptions
from functions.colors import *

def main():
    show_banner()

    try:
        user_password_length = int(input("Tamanho da senha: (Recomendado: 8 até 50)\n>>> "))

    except KeyboardInterrupt as ki:
        exceptions.keyboard_interrupt(ki)

    except Exception as error:
        exceptions.exception(error)
    
    else:
        print("Gerando senha...")

    print(f"Senha gerada: {bold + password_generator(user_password_length) + reset}")

if __name__ == '__main__':
    main()
