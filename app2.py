from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Praça','Comida Brasileira')
#restaurante_praca.receber_avaliacao('João', 5)
#restaurante_praca.receber_avaliacao('Maria', 4.3)
#restaurante_praca.receber_avaliacao('José', 9)
#restaurante_praca.alternar_estados = True
#restaurante_pizza = Restaurante('Pizza Hut','Pizzaria')
#restaurante_japones = Restaurante('Sushi House','Japonesa')
bebida_coca = Bebida('Coca-Cola', 5.5, '600ml')
bebida_suco = Bebida('Suco de Laranja', 4.5, '300ml')


prato_pao = Prato('Pão de Queijo', 3.5, 'Pão de queijo mineiro')
prato_pao.aplicar_desconto()
bebida_coca.aplicar_desconto()
restaurante_praca.adicionar_item(bebida_coca)
restaurante_praca.adicionar_item(prato_pao)

def main():
    #Restaurante.listar_restaurantes()
    restaurante_praca.listar_itens
    


if __name__ == '__main__':
    main()

#Criar ambiente virtual: python -m venv venv
#Ativar ambiente virtual: source venv/bin/activate
#pip freeze > requirements.txt
#Instalar dependências: pip install -r requirements.txt