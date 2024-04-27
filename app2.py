from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça','Comida Brasileira')
restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Maria', 4.3)
restaurante_praca.receber_avaliacao('José', 9)
#restaurante_praca.alternar_estados = True
#restaurante_pizza = Restaurante('Pizza Hut','Pizzaria')
#restaurante_japones = Restaurante('Sushi House','Japonesa')



def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()