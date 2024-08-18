"""
Pseudocódigo:
INICIO
- mostrar o nome do programa "Calculadora Básica" com fonte diferenciada;
- Solicitar o primeiro número a ser calculado e armazenar na memória;
- Solicitar o segundo número a ser calculado e armazenar na memória;
- Solcitar que o usuário informe a operação que deseja executar e armazene na memória;
- Comparar o operador escolhido com as opções e efetuar o cálculo.
- Mostrar o resultado para o usuário;
FIM
"""

print('''
╔═══╗──╔╗──────╔╗─────╔╗─────╔══╗
║╔═╗║──║║──────║║─────║║─────║╔╗║
║║─╚╬══╣║╔══╦╗╔╣║╔══╦═╝╠══╦═╗║╚╝╚╦══╦══╦╦══╦══╗
║║─╔╣╔╗║║║╔═╣║║║║║╔╗║╔╗║╔╗║╔╝║╔═╗║╔╗║══╬╣╔═╣╔╗║
║╚═╝║╔╗║╚╣╚═╣╚╝║╚╣╔╗║╚╝║╚╝║║─║╚═╝║╔╗╠══║║╚═╣╔╗║
╚═══╩╝╚╩═╩══╩══╩═╩╝╚╩══╩══╩╝─╚═══╩╝╚╩══╩╩══╩╝╚╝''')

numero_01 = float(input('Insira o primeiro número: '))
numero_02 = float(input('Insira o segundo número: '))

operacao = input('Escolha uma das quatro operações básicas (+, -, *, /): ')
match operacao:
    case "+":
        resultado = numero_01 + numero_02
        print(f'O resultado da soma é: {resultado}')
    case "-":
        resultado = numero_01 - numero_02
        print(f'O resultado da subtração é: {resultado}')
    case "*":
        resultado = numero_01 * numero_02
        print(f'O resultado da multiplicação é: {resultado}')
    case "/":
        if numero_02 != 0:
            resultado = numero_01 / numero_02
            print(f'O resultado da divisão é: {resultado}')
        else:
            print('Erro: divisão por zero não é permitida')
    case _:
        print('Operação inválida')