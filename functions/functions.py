from functions.colors import *
from platform import python_version_tuple
from string import ascii_letters as all_letters, digits as all_numbers
from secrets import choice
from itertools import count
from functions import exceptions

import sys

# define oque * irá importar desse arquivo
__all__ = ['show_banner', 'password_generator', 'version_check', 'confirm']


def version_check():
    python_version_major = int(python_version_tuple()[0])
    python_version_minor = int(python_version_tuple()[1])

    if python_version_major == 3:
        if python_version_minor < 9:
            print(vermelho + "Python 3.9 ou acima" + reset)
            print(vermelho + "Encerrando..." + reset)
            sys.exit(1)
        else:
            pass

    elif python_version_major > 3: 
        pass

    else:
        print(vermelho + "Python 3.9 ou acima" + reset)
        print(vermelho + "Encerrando..." + reset)
        sys.exit(1)


def show_banner() -> str:
    ascii_art = '''
._._._._._._._._._|__________________________________________________________,
|_|_|_|_|_|_|_|_|_|_________________________________________________________/
                  |                                                            
'''
    print("")
    print(vermelho + bold + ascii_art + reset)
    print("")
    print(amarelo + bold + "Password Generator v1.5" + reset)
    print(amarelo + bold + "-"*30 + reset)
    print(amarelo + bold + "GitHub: https://github.com/sa1n255" + reset)
    print(amarelo + bold + "Coded by Sa1n" + reset)
    print("")


def confirm():
    confirmar = input("Você tem certeza que deseja prosseguir mesmo assim? [Y/n]: ").lower()
    if 'y' in confirmar or 's' in confirmar:
        print(verde + 'Prosseguindo' + reset)
        return True
    else:
        print("Abortando")
        return False


def password_generator(password_lenght: int = 8) -> str:
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reduced_punctuation = '&$%#@'
    all_options = all_letters + all_numbers + reduced_punctuation

    try:
        while True:

            # 1- A Senha do Usuario sempre deve começar com letra Maiuscula
            # 2- A Senha do Usuario sempre deve conter números
            # 3- A Senha do Usuario sempre deve conter pontuações
            # 4- A Senha do Usuário nunca deve ter mais de dois caracteres repetidos

            user_password = ""
            user_password += choice(upper_letters)

            # Gera a senha
            for i in range(password_lenght-1): user_password += choice(all_options)

            # Checa se a senha gerada tem Números
            for i in all_numbers: 
                if i not in user_password: password_has_number = False
                else:
                    password_has_number = True
                    break

            # Checa se a senha gerada tem Letras
            for i in all_letters:
                if i not in user_password: password_has_letters = False
                else:
                    password_has_letters = True
                    break

            # Checa se a senha gerada tem Pontuações
            for i in reduced_punctuation:
                if i not in user_password: password_has_punc = False
                else:
                    password_has_punc = True
                    break

            # Checa se a senha gerada tem mais de 2 caracteres repetidos
            for i in user_password:
                if user_password.count(i) > 2:
                    too_many_characters = True
                    break
                else: too_many_characters = False
        
            phn, php, phl, tmc = password_has_number, password_has_punc, password_has_letters, too_many_characters
            # Checa se a senha gerada atende os 4 requisitos
            if (phn == True and php == True and phl == True and tmc == False) == True:
                return user_password

    except KeyboardInterrupt as ki: 
        exceptions.keyboard_interrupt(ki)

    except Exception as error: 
        exceptions.exception(error)
