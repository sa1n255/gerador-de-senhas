from functions.colors import *
from string import ascii_letters as all_letters, digits as all_numbers
from secrets import choice
from itertools import count
from functions import exceptions

# define oque * irá importar
__all__ = ['show_banner', 'password_generator', ]


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


def password_generator(password_lenght: int = 8) -> str:
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reduced_punctuation = '&$%#@'
    all_options = all_letters + all_numbers + reduced_punctuation
    try:
        while True:

            # A Senha do Usuario sempre deve começar com letra Maiuscula
            # A Senha do Usuario sempre deve conter números
            # A Senha do Usuario sempre deve conter pontuações
            # A Senha do Usuário nunca deve ter mais de dois caracteres repetidos

            user_password = ""
            user_password += choice(upper_letters)

            for i in range(password_lenght-1):
                user_password += choice(all_options)
            # Checa se a senha tem Números
            for i in all_numbers:
                if i not in user_password:
                    password_has_number = False
                else:
                    password_has_number = True
                    break
            # Checa se a senha tem Letras
            for i in all_letters:
                if i not in user_password:
                    password_has_letters = False
                else:
                    password_has_letters = True
                    break
            # Checa se a senha tem Pontuações
            for i in reduced_punctuation:
                if i not in user_password:
                    password_has_punc = False
                else:
                    password_has_punc = True
                    break
            # Checa se a senha tem muitos caracteres repetidos
            for i in user_password:
                if user_password.count(i) > 2:
                    too_many_characters = True
                    break
                else:
                    too_many_characters = False
            if (password_has_number == True and password_has_punc == True and password_has_letters == True and too_many_characters == False) == True:
                return user_password
            else:
                pass

    except KeyboardInterrupt as ki:
        exceptions.keyboard_interrupt(ki)

    except Exception as error:
        exceptions.exception(error)
