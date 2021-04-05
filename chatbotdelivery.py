import time
import pickle

#abrindo arquivo para escrita e criando no diretorio
#arquivoNovo = 'dados_clientes'
#arquivoNovo = open(arquivoNovo,'wb')


# classe pai
class cliente():
    def __init__(self,tel,nome,end):
        self.nome = nome
        self.tel = tel
        self.end = end
        print(nome, tel)
        
# classe filho
class pedido(cliente):
    def __init__(self, nome, tel,end, pizza ='vazio'):
        cliente.__init__(self, nome, tel,end)
        self.pizza = pizza


    def fazerPedido(self, pizza, sabor):
        setattr(self, pizza, sabor)

    def pedidopronto(self):
        return [self.nome, self.tel,self.end, self.pizza]

def main():
    dateComplet = time.ctime()
    dataDict = dateComplet.split()
    justHour = dataDict[3]
    justHour = justHour.split(':')
    justHour = int(justHour[0])
    if justHour > 13:
        print('Boa tarde')
    elif justHour > 18:
        print('Boa noite')
    else:
        print('Bom dia')
    print('Bem vindo a pizzaria do seu zé!, Para começarmos Por favor digite seu contato com o prefixo sem espaços')
    
    
    nome, endereco, resposta, idCliente = verificaCadastro(validaTelefone())
    #dadosCliente = {idCliente:{'nome':nome,'tel':idCliente,'end':endereco}}
    #cadastrando meu cliente
    if resposta == 'sim':  
        cadastraCliente(dadosCliente)
        print('Cliente Cadastrado')
    else:
        print(nome, endereco, resposta, idCliente)
      

def validaTelefone():
    valid = True
    while valid == True:
        tel = input('')
        qntNum = len(tel)
        if not tel.isdigit():
            print("Digite apenas numeros!")
        else:
            if qntNum < 11:
                print('ops acho que você digitou numero a menos!')
            elif qntNum > 11:
                print('ops acho que você digitou numero a mais!')
            else:
                valid = False
    return tel

def verificaCadastro(self,info):
    self.idCliente = info
    arquivoLer = pickle.load(open( "dados_clientes", "rb" ) )
    if idCliente in arquivoLer:
        print(arquivoLer[idCliente])
    else:
        self.resposta = input('Você ainda não tem cadastro deseja fazerum? Sim ou Não')
        if self.resposta == 'sim':
            self.nome = input('Digite seu Nome: ')
            self.endereco = input('Digite seu endereço: ')
        else:
            print('Tudo bem, preciso de algumas informações para entrega')
            self.nome = input('Digite seu Nome: ')
            self.endereco = input('Digite seu endereço: ')
    return (self.nome,self.endereco,self.resposta,self.idCliente)
        
def cadastraCliente(info):
    idCliente = info
    pickle.dump(idCliente,arquivoNovo)
    arquivoNovo.close()
main()
