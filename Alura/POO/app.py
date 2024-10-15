from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('LaPlaza', 'Gourmet')
restaurante_pizza = Restaurante('DonPizza', 'Pizzaria')
restaurante_hamburger = Restaurante('MrBurquer', 'Hamburgueria')

restaurante_hamburger.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()