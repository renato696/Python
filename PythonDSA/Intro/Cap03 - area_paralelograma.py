"""
Pseudocódigo:
- Exiba 'Bem-vindo a Calculadora de Área do Paralelograma;
- Peça para o usuário inserir o comprimento da base;
- Armazene o comprimento da base em uma variável;
- Peça para o usuário inserir a altura;
- Armazene o resultado em uma variável;
- Calcule a área do paralelograma: base * altura
- Exiba o resultado
"""

print('Bem-vindo à Calculadora de Área do Paralelograma')
base = float(input('Insira o comprimento da base: '))
altura = float(input('Insira a altura: '))
area = base * altura
print(f'A área do paralelograma é: {area}')
