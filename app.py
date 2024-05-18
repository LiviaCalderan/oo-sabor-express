from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelo.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5, 'grande')
prato_macarrao = Prato('Macarrão c/ Bolonhesa', 25, 'O melhor molho da cidade')
restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_macarrao)

def main():
    pass

if __name__ == '__main__' :
    main()