from functions.colors import *
import sys


def keyboard_interrupt(ki):
    ki = "KeyboardInterrupt: Você interrompeu a execução"
    print("")
    print(amarelo + ki + reset)
    print(vermelho + "Encerrando..." + reset)
    sys.exit(0)


def exception(error):
    error = 'Erro: Você só pode digitar números'
    print(vermelho + error + reset)
    print(vermelho + "Encerrando..." + reset)
    sys.exit(1)
