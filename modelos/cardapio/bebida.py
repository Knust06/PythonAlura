from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho
