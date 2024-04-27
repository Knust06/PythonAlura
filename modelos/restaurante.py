from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"Restaurante {self._nome} - Categoria {self._categoria}"
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_notas = sum([avaliacao._nota for avaliacao in self._avaliacao])
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media

    @classmethod   
    def listar_restaurantes(cls):
        for i in cls.restaurantes:
            print(f"Nome: {i._nome.ljust(25)} | Categoria: {i._categoria.ljust(25)} | Ativo: {i.ativo.ljust(25)} | Avaliação: {i.media_avaliacoes}")

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    @ativo.setter
    def alternar_estados(self, novo_estado):
        self._ativo = novo_estado

    def receber_avaliacao(self, cliente,avaliacao):
        if 0 < avaliacao <= 5:
            avaliacao = Avaliacao(cliente, avaliacao)
            self._avaliacao.append(avaliacao)


    