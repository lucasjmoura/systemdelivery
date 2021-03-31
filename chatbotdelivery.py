# classe pai
class cliente():
    def __init__(self, nome, tel):
        self.nome = nome
        self.tel = tel
        print('criou a classe')
        print(nome, tel)

    # classe filho
class pedido(cliente):
    def __init__(self, nome, tel, lanche="vazio", batata="vazio", refri="vazio"):
        cliente.__init__(self, nome, tel)
        self.lanche = lanche
        self.batata = batata
        self.refri = refri

    def fazerPedido(self, produto, valor):
        setattr(self, produto, valor)

    def pedidopronto(self):
        return [self.nome, self.tel, self.lanche, self.batata, self.refri]

pedido1 = pedido('lucas', '43425245')
pedido1.fazerPedido("lanche",'xburguer')
pedido1.pedidopronto()

pedido2 = pedido('carlos', '43425245')
pedido1.fazerPedido("lanche",'xsalada')
pedido1.pedidopronto()
