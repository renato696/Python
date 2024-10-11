class Restaurante:
    def __init__(self, nome, categoria):
        nome = ''
        categoria = ''
        ativo = False
    
restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

print(dir(restaurante_praca))
    