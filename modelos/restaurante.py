from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #self - trata o obejto que esta vindo 
        self._nome = nome.title() #para deixar a primeira letra maiuscula
        self._categoria = categoria.upper() #pode usar 'this' ao inves do 'self'
        self._ativo = False #atributo protegido _ativo
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) #toda vez que criar o obj ele é add a lista

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Statos'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}| {restaurante.ativo}')

    @property
    def ativo(self):
        return '▣' if self._ativo else '▢'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1) # o '1'é a quant de casas decimais
        return media
    
    def adicionar_bebida_no_cardapio(self, bebida):
        self._cardapio.append(bebida)

    def adicionar_prato_no_cardapio(self, prato):
        self._cardapio.append(prato)