import sys
from datetime import datetime


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self._nome = nome
        self._telefone = telefone
        self._endereco = endereco

    def get_telefone(self):
        return self._telefone

    def get_endereco(self):
        return self._endereco

    def get_nome(self):
        return self._nome

    def set_telefone(self, novo_telefone):
        self._telefone = novo_telefone

    def set_endereco(self, novo_endereco):
        self._endereco = novo_endereco

    def set_nome(self, novo_nome):
        self._nome = novo_nome


class Produto:
    def __init__(self, quantidade=1):
        self._quantidade = quantidade

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade


class Pizza(Produto):
    def __init__(self, sabor, quantidade):
        super().__init__(quantidade)
        self._sabor = sabor

    def get_sabor(self):
        return self._sabor

    def set_sabor(self, new_sabor):
        self._sabor = new_sabor

    def __repr__(self):
        return f'Sabor: {self._sabor}\nQuantidade: {self._quantidade}'


class Pedido:
    control_id = 0

    def __init__(self, cliente: Cliente, data_pedido, hora_inicio, hora_final, lista_de_produtos):
        self._data_pedido = data_pedido
        self._data_inicio = hora_inicio
        self._data_final = hora_final
        self._produto = lista_de_produtos
        self._pessoa: Cliente = cliente
        self.control_idd = self.gerar_id()

    def nota_fiscal(self):
        return self._pessoa.get_telefone()

    def __repr__(self):
        return f'\n============================================ ' \
               f'\nData de realização: {self._data_pedido}' \
               f'\nPedido numero:{self.control_idd} - Realizado: {self._data_inicio} ' \
               f'\nEm nome de: {self._pessoa.get_nome()} ' \
               f'\nPizzas:\n{self.converter()} ' \
               f'\nPedido finalizado:{self._data_final}' \
               f'\n============================================'

    def converter(self):
        return '\n'.join(str(itens) for itens in self._produto)

    def get_data_inicio(self):
        return self._data_inicio

    def get_data_final(self):
        return self._data_final

    def get_produto(self):
        return self._produto

    def get_telefone(self):
        return self._pessoa.get_telefone()

    @classmethod
    def gerar_id(cls):
        cls.control_id += 1
        return cls.control_id


class Utils:
    mensagem = {'dia': 'Bom dia', 'trade': 'Boa tarde', 'noite': 'Boa noite',
                'entrada_telefone': 'Por favor digite o telefone do cliente com o prefixo e sem espaços:\n',
                'alerta_erro': 'Ops acho que você digitou algo errado, tente novamente!\n',
                'entrada_nome': 'Favor informe seu nome:\n',
                'entrada_endereco': 'Favor informe um endereço para entrega:\n',
                'alteracao_pedido': 'Gostaria de alterar o sabor(1), ou a quantidade(2), favor utilize os indices '
                                    'para responder\n',
                'alteracao_dados': 'Gostaria de alterar o nome(1), ou o telefone(2), favor utilize os indices '
                                    'para responder\n',
                'mudar_sabor': 'Informe o novo sabor:\n',
                'mudar_quantidade': 'Informe a nova quantidade:\n',
                'alterar_pedido': 'Deseja fazer alguma alteração no pedido, (responda sim ou não):\n',
                'mudar_nome': '\nInforme o novo nome:\n  ',
                'mudar_endereco': 'Informe o novo endererco:\n',
                'informe_sabor': 'Informe o sabor da Pizza:\n', 'informe_quantidade': 'Informe a quantidade:\n',
                'mudar_pedido': 'Deseja alterar o pedido?\n',
                'confirmacao_dados_cliente': '\nEste numero já possui cadastro!'}

    #  TODO retornar a hora ou a data
    @classmethod
    def data_hora(cls, index):
        busca = {'data': '%d/%m/%y', 'hora': '%X'}
        cls._data = datetime.now().strftime(busca[index])
        return cls._data


class ValidaRevisa:

    @classmethod
    def revisar_produto(cls, sabor_informado, lista_de_pizzas):
        busca = (resultado for resultado in lista_de_pizzas if resultado.get_sabor() == sabor_informado)
        resultado_busca = next(busca, None)
        if resultado_busca is not None:
            alteracao = input(Utils.mensagem['alteracao_pedido'])
            if alteracao == '1':
                novo_sabor = input(Utils.mensagem['mudar_sabor'])
                resultado_busca.set_sabor(novo_sabor)
                print('Sabor', sabor_informado, 'alterado para ', resultado_busca.get_sabor())
            elif alteracao == '2':
                quantidade_anterior = resultado_busca.get_quantidade()
                nova_quantidade = input(Utils.mensagem['mudar_quantidade'])
                resultado_busca.set_quantidade(nova_quantidade)
                print('Quantidade', quantidade_anterior, 'alterado para ', resultado_busca.get_quantidade())
        else:
            print('O sabor informado não exite no pedido')


    @classmethod
    def valida_cliente(cls, telefone, lista_clientes):
        busca = (resultado for resultado in lista_clientes if resultado.get_telefone() == telefone)
        resultado_busca = next(busca, None)
        if resultado_busca is not None:
            return resultado_busca.get_nome(), resultado_busca.get_endereco()
        else:
            print('\nEste numero ainda não foi cadastrado')
            return False

    @classmethod
    def alterar_cadastro(cls,telefone, lista_clientes):
        busca = (resultado for resultado in lista_clientes if resultado.get_telefone() == telefone)
        resultado_busca = next(busca, None)
        alteracao = input(Utils.mensagem['alteracao_dados'])
        if alteracao == '1':
            nome_anterior = resultado_busca.get_nome()
            novo_nome = input(Utils.mensagem['mudar_nome'])
            resultado_busca.set_nome(novo_nome)
            print('Nome ', nome_anterior, 'alterado para ', novo_nome)
        elif alteracao == '2':
            endereco_anterior = resultado_busca.get_endereco()
            novo_endereco = input(Utils.mensagem['mudar_endereco'])
            resultado_busca.set_endereco(novo_endereco)
            print('Endereçoo', endereco_anterior, 'alterado para ', resultado_busca.get_endereco())
        return resultado_busca.get_nome(), resultado_busca.get_endereco()


    @classmethod
    def consulta_pedido_numero(cls, id, lista_pedidos):
        busca = (resultado for resultado in lista_pedidos if resultado.control_idd == id)
        resultado_busca = next(busca, None)
        if resultado_busca is not None:
            print(resultado_busca)
        else:
            print('Ops, não encontramos esse pedido')
            return False

    @classmethod
    def consulta_pedido_telefone(cls, id, lista_pedidos):
        busca = (resultado for resultado in lista_pedidos if resultado.get_telefone() == id)
        todos_pedidos = list(busca)
        if len(todos_pedidos) != 0:
            print('\n', todos_pedidos)

            return True
        else:
            return False

    @classmethod
    def valida_telefone(cls, telefone):
        numero = len(telefone)
        if not telefone.isdigit():
            print(Utils.mensagem['alerta_erro'])
            return False
        elif numero < 11 or numero > 11:
            print(Utils.mensagem['alerta_erro'])
            return False
        return telefone


class Gerenciamento:
    lista_pedidos = []
    lista_clientes = []

    @classmethod
    def cria_pedido(cls):
        data_pedido = Utils.data_hora('data')
        hora_inicial = Utils.data_hora('hora')
        lista_de_produtos = []
        while True:
            telefone = cls.coleta_dados(Utils.mensagem['entrada_telefone'])
            telefone = ValidaRevisa.valida_telefone(telefone)
            if telefone:
                break
        if ValidaRevisa.valida_cliente(telefone, cls.lista_clientes) is False:
            nome = cls.coleta_dados(Utils.mensagem['entrada_nome'])
            endereco = cls.coleta_dados(Utils.mensagem['entrada_endereco'])
            cliente = Cliente(nome, telefone, endereco)
            cls.lista_clientes.append(cliente)
        else:
            nome, endereco = ValidaRevisa.valida_cliente(telefone, cls.lista_clientes)
            print(Utils.mensagem['confirmacao_dados_cliente'])
            print('Nome: ', nome, '\nendereco: ', endereco)
            while True:
                atualizar = cls.coleta_dados('Você deseja altulizar os dados?')
                if atualizar == 'sim':
                    ValidaRevisa.alterar_cadastro(telefone,cls.lista_clientes)
                else:
                    break

            cliente = Cliente(nome, telefone, endereco)

        while True:
            sabor = cls.coleta_dados(Utils.mensagem['informe_sabor'])
            quantidade = int(cls.coleta_dados(Utils.mensagem['informe_quantidade']))
            pizza = Pizza(sabor, quantidade)
            lista_de_produtos.append(pizza)
            if cls.coleta_dados('Você deseja fazer outro pedido?\n') != 'sim':
                break

        while True:
            if cls.coleta_dados(Utils.mensagem['mudar_pedido']) != 'sim':
                break
            ValidaRevisa.revisar_produto(cls.coleta_dados('informe o sabor da pizza a ser alterada:!\n'),
                                         lista_de_produtos)

        hora_final = Utils.data_hora('hora')
        pedido = Pedido(cliente, data_pedido, hora_inicial, hora_final, lista_de_produtos)
        return pedido

    @classmethod
    def coleta_dados(cls, entrada):
        saida = input(entrada)
        return saida

    @classmethod
    def menu(cls):
        while True:
            print('\nBem vindo ao sistema de gerenciamento de pedidos e clientes da Pizzaria São José!!')
            escolha_menu = cls.coleta_dados('Para prosseguirmos utilize os indices para escolher uma opção abaixo!'
                                            '\nRealizar Pedido:(1)'
                                            '\nRastrear um pedido por numero ou por telefone:(2)'
                                            '\nSair(3)'
                                            '\nIndice: ')
            if escolha_menu == '1':
                pedido = cls.cria_pedido()
                cls.lista_pedidos.append(pedido)

            elif escolha_menu == '2':
                consulta = cls.coleta_dados('Informe um numero do pedido ou um telefone cadastrado:!\n')
                #  TODO verificar o resultado aqui
                if ValidaRevisa.consulta_pedido_telefone(consulta, cls.lista_pedidos) is False:
                    ValidaRevisa.consulta_pedido_numero(int(consulta), cls.lista_pedidos)
            elif escolha_menu == '3':
                sys.exit()
            else:
                'Essa opção não existe'


if __name__ == '__main__':
    Gerenciamento.menu()
