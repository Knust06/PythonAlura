class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f"Restaurante {self.nome} - Categoria {self.categoria}"

    def listar_restaurantes():
        for i in Restaurante.restaurantes:
            print(f"Nome: {i.nome} | Categoria: {i.categoria} | Ativo: {'Sim' if i.ativo else 'Não'}")

restaurante_praca = Restaurante('Praça','Comida Brasileira')
restaurante_pizza = Restaurante('Pizza Hut','Pizzaria')


Restaurante.listar_restaurantes()
