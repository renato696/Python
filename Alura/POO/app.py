from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('LaPlaza', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
prato_omelete = Prato('Omelete', 20.00, 'Ovos mexidos com tomate e oregano')


#restaurante_praca.receber_avaliacao('Renato', 1)
#restaurante_praca.receber_avaliacao('Kosuke', 2)
#restaurante_praca.receber_avaliacao('Amora', 6)
#restaurante_pizza = Restaurante('DonPizza', 'Pizzaria')
#restaurante_hamburger = Restaurante('MrBurquer', 'Hamburgueria')

#restaurante_hamburger.alternar_estado()

def main():
    print(bebida_suco)
    print(prato_omelete)
    #Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()