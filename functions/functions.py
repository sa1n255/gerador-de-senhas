from random import choice
from string import ascii_letters, digits, punctuation

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
reset = '\033[0;0m'
bold = '\033[1m'


def banner():
    ascii_art = '''
._._._._._._._._._|__________________________________________________________,
|_|_|_|_|_|_|_|_|_|_________________________________________________________/
                  |
'''
    print("")
    print(vermelho + bold + ascii_art + reset)
    print("")
    print(amarelo + bold + "Password Generator v1.0" + reset)
    print(amarelo + bold + "-"*30 + reset)
    print(amarelo + bold + "GitHub: https://github.com/sa1n255" + reset)
    print(amarelo + bold + "Coded by Sa1n" + reset)
    
    # print(amarelo + bold + "" + reset)
    print("")


def password_generator(passwd_len = 8):
    ascii_options = ascii_letters
    number_options = digits
    punt_options = punctuation
    options = ascii_options + number_options + punt_options

    user_password = ""

    for i in range(0, passwd_len):
        digit = choice(options)
        user_password += digit

    return user_password
