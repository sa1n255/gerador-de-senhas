from functions.functions import password_generator, banner, reset, vermelho, bold

banner()
user_choice = input("Quantos digitos você quer na sua senha? ")

if user_choice.isdigit():
    user_choice = int(user_choice)
else:
    print(vermelho + "Input inválido, irmão!" + reset)
    print(vermelho + "Encerrando..." + reset)
    quit()

output_password_generator = password_generator(user_choice)
print(f"Senha gerada: {bold + output_password_generator + reset}")
