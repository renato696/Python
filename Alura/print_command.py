#print ('Python na Escola de Programação Alura\n')

#nome = input ('Qual é o seu nome: ')
#idade = input ('Qual é a sua idade:')

#Abordagem mais simples
#print('Meu nome é ',nome, 'e tenho', idade, 'anos')

#Abordagem do f-string
#print (f'Meu nome é {nome} e tenho {idade} anos\n')

#Abordagem do .format()
#print ('Meu nome é {} e tenho {} anos.' .format(nome,idade))


#print ("""
#A
#L
#U
#R
#A
#""")

#print ('A','L','U','R','A', sep '/n')


#imprimir pi=3.14159 arredondado em duas casas decimais
pi = 3.14159

#Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

#Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

#Utilizando a função round()
print('O valor arredondado de pi é' ,round(pi,2))

