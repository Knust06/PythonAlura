class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Restaurante da Praça'
restaurante_praca.categoria = 'Prato Feito'
restaurante_praca.ativo = False

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizzaria do João'
restaurante_pizza.categoria = 'Pizza'
restaurante_pizza.ativo = True

print(vars(restaurante_praca))
