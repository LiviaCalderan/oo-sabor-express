from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #HERANÇA
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #super - permite que acesse info de outra class
        self._descricao = descricao

    def __str__(self):
        return self._nome