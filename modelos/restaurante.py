class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"Restaurante {self._nome} - Categoria {self._categoria}"

    @classmethod   
    def listar_restaurantes(cls):
        for i in cls.restaurantes:
            print(f"Nome: {i._nome.ljust(25)} | Categoria: {i._categoria.ljust(25)} | Ativo: {i.ativo.ljust(25)}")

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    @ativo.setter
    def alternar_estados(self, novo_estado):
        self._ativo = novo_estado

restaurante_praca = Restaurante('Praça','Comida Brasileira')
restaurante_praca.alternar_estados = True
restaurante_pizza = Restaurante('Pizza Hut','Pizzaria')

Restaurante.listar_restaurantes()


    