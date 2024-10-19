from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('LaPlaza', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
bebida_suco.aplica_desconto()
prato_omelete = Prato('Omelete', 20.00, 'Ovos mexidos com tomate')
prato_omelete.aplica_desconto()
restaurante_praca.adicionar_ao_cardapio(bebida_suco)
restaurante_praca.adicionar_ao_cardapio(prato_omelete)

#restaurante_praca.receber_avaliacao('Renato', 1)
#restaurante_praca.receber_avaliacao('Kosuke', 2)
#restaurante_praca.receber_avaliacao('Amora', 6)
#restaurante_pizza = Restaurante('DonPizza', 'Pizzaria')
#restaurante_hamburger = Restaurante('MrBurquer', 'Hamburgueria')

#restaurante_hamburger.alternar_estado()

def main():
   restaurante_praca.exibir_cardapio
    #Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()