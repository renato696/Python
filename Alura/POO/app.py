from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('LaPlaza', 'Gourmet')
restaurante_praca.receber_avaliacao('Renato', 8)
restaurante_praca.receber_avaliacao('Kosuke', 10)
restaurante_praca.receber_avaliacao('Amora', 7)
#restaurante_pizza = Restaurante('DonPizza', 'Pizzaria')
#restaurante_hamburger = Restaurante('MrBurquer', 'Hamburgueria')

#restaurante_hamburger.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()