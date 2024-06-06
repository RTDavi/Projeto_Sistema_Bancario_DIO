from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty

class Conta:
    
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._cliente = cliente
        self._numero_agencia = "0001"
        self._historico = Historico()
    
    
    @property
    def saldo_valor(self):
        saldo = self._saldo

        return saldo
    

    @property
    def numero_conta(self):
        numero_conta = self._numero_conta

        return numero_conta
    

    @property
    def cliente(self):
        cliente_nome = self._cliente

        return cliente_nome["nome"]
    

    @property
    def agencia(self):
        agencia = self._numero_agencia

        return agencia
    

    @property
    def historico(self):
        return self._historico
    

    @classmethod
    def nova_conta(cls, numero_conta, cliente):
        nomes = [nomes["nome"] for nomes in cliente]

        for cliente_nome in nomes:
            cls.conta = {"Número da conta":numero_conta,
                    "Nome do Cliente": cliente_nome}

        return cls.conta
    

    def depositar(self, valor_deposito):

        if valor_deposito > 0 :
            self._saldo += valor_deposito
            
            print(f"\nVOCÊ DEPOSITOU R${valor_deposito:.2f}, SEU SALDO ATUAL É DE: {self.saldo_valor:.2f}")
            return True
        

        else:
            print("\n NÃO É POSSÍVEL DEPOSITAR VALORES NEGATIVOS")
            return False


    def sacar(self, valor_saque):
        saldo = self.saldo_valor

        if valor_saque > saldo:
            print("\n[NÃO FOI POSSíVEL CONCLUIR A TRANSAÇÃO, SALDO INSUFICIENTE.]")

            return False
        

        elif valor_saque > 0:
            self._saldo -= valor_saque

            print(f"\n[TRANSAÇÃO CONCLUÍDA, SALDO ATUAL É DE: {self.saldo_valor:.2f}]")
            return True
        

        else:
            print("NÃO FOI POSSíVEL REALIZAR A TRANSAÇÃO, DIGITE UM VALOR VÁLIDO.")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero_conta, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
    

    def saque(self, valor_saque):
        limite_transacoes = [len(transacao) for transacao in self.historico.transacoes
                             if transacao["Tipo de Transação"] == "Saque"]

        if self.limite_saque > limite_transacoes:
            print("LIMITE DE SAQUES EXCEDIDO, TENTE NOVAMENTE MAIS TARDE.")
        

        if valor_saque > self.limite:
            print("VALOR DO SAQUE EXCEDIDO, TENTE COM UM VALOR ABAIXO DE 500R$.")
        

        else:
            return super().sacar(valor_saque)


class Historico:

    def __init__(self):
        self._transacao_historico = []
    

    @property
    def transacoes(self):
        return self._transacao_historico
    

    def adicionar_transacao(self, tipo_transacao, transacao):
       transacoes = self._transacao_historico

       transacoes.append({
           "Tipo de Transação": tipo_transacao,
           "Valor Transação": transacao
           })

       return transacoes
        

class Cliente:
    def __init__(self, endereço):
        self._endereço = endereço
        self._contas = []


    @property
    def endereços(self):
        return self._endereço
    

    @property
    def contas(self):
        return self._contas


    def adicionar_conta(self, conta):
        self._contas.append(conta)

    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class Transacao(ABC):
    @classmethod
    @abstractmethod
    def registrar(self,conta):
        pass
    
    @property
    @abstractmethod
    def valor(self):
        pass


class Saque(Transacao):
    def __init__(self, valor_saque, conta):
        self._valor_saque = valor_saque
        self.conta = conta

    def registrar(self):
        if self.conta.sacar(self._valor_saque):
            self.conta.historico.adicionar_transacao("Saque", self._valor_saque)


    @property
    def valor(self):
        valor = self._valor_saque
        return valor
    

class Depósito(Transacao):
    def __init__(self, valor_deposito, conta):
        self._valor_deposito = valor_deposito
        self.conta = conta
    
    @property
    def valor(self):
        valor = self._valor_deposito
        return valor

    def registrar(self):
        if self.conta.depositar(self._valor_deposito):
            self.conta.historico.adicionar_transacao("Depósito", self._valor_deposito)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        super().__init__(endereco)


def criar_usuario(usuarios):

    cpf = input("""
    ############## BEM VINDO AO MENU BANCARIO ############## 

    PARA CRIAR SUA CONTA PRECISAREMOS DE ALGUMAS INFORMAÇÕES,
    DIGITE SEU CPF(xxx.xxx.xxx-xx).
    => """)
    cpf_filtro = filtrar_cpf(cpf, usuarios)

    if cpf_filtro == True:
        print("JÁ EXISTE UM USUÁRIO CADASTRADO COM ESTE CPF!")
        return
    
    else:
        nome_usuario = input("\n     AGORA, O SEU NOME:\n => ")
        data_de_nascimento = input("\n    AGORA, DIGITE SUA DATA DE NASCIMENTO(dd/mm/ano):\n => ")
        endereco = input("\n     DIGITE SEU ENDEREÇO(nome da rua, numero - bairro- cidade/sigla estado): \n => ")

        usuarios.append({
            "nome":nome_usuario,
            "data_nascimento": data_de_nascimento,
            "cpf": cpf, 
            "endereco": endereco
            })


def filtrar_cpf(cpf, usuarios):
   for usuario in usuarios:
       print(usuario["cpf"])
       if usuario["cpf"] == cpf:
            return True
       else:
           return False


def ver_extrato(saldo, extrato):
    deposito_contador = 0
    saque_contador = 0

    print("############## EXTRATO ##############")
    print("\nDEPÓSITOS:")
    for deposito in extrato:
        if deposito["Tipo de Transação"] == "Depósito":
            valor_deposito = deposito["Valor Transação"]
            deposito_contador += 1
            print(f"DEPÓSITO {deposito_contador}: R${valor_deposito}")
        

    print("\nSAQUES:")
    for saque in extrato:
        if saque["Tipo de Transação"] == "Saque":
            valor_saque = saque["Valor Transação"]
            saque_contador += 1
            print(f"SAQUE {saque_contador}: R${valor_saque}")


    print(f"\nSALDO ATUAL: R${saldo:.2f}")
    print("#####################################")


def lista_contas(contas):
    contador = 0

    print("""############## CONTAS BANCARIAS ##############""")
    for conta in contas:
        contador += 1
        nome_conta = conta["Nome do Cliente"]
        numero_conta = conta["Número da conta"]

        print(f"CONTA DE NÚMERO: {numero_conta}. DONO DA CONTA: {nome_conta}")
    

def menu_bancario():
    menu_bancario = f"""
   ############## BEM VINDO AO MENU BANCARIO ##############

   [1] DEPOSITAR
   [2] SACAR
   [3] VER EXTRATO BANCÁRIO
   [4] CRIAR UM USUARIO
   [5] CRIAR UMA CONTA
   [6] VER LISTA DE CONTAS
   [7] SAIR

   ########################################################

   ESCOLHA UMA OPÇÃO: """
    return input(menu_bancario)


def main():
    clientes = []
    contas = []
    conta = Conta(len(contas), clientes)

    while True:
        escolha = menu_bancario()

        if escolha == '1':
            cpf = input("DIGITE SEU CPF NOVAMENTE (xxx.xxx.xxx-xx): ")
            cpf_filtro = filtrar_cpf(cpf, clientes)

            if cpf_filtro == True:
                valor_deposito = int(input("DIGITE O VALOR A SER DEPOSITADO: "))
                deposito = Depósito(valor_deposito, conta)
                deposito.registrar()


            else:
                print("USUÁRIO NÃO ENCONTRADO, TENTE CRIAR UM USUÁRIO E UMA CONTA PARA PODER SACAR.")
        


        if escolha == '2':
            cpf = input("DIGITE SEU CPF NOVAMENTE (xxx.xxx.xxx-xx): ")
            cpf_filtro = filtrar_cpf(cpf, clientes)

            if cpf_filtro == True:
                valor_saque = int(input("DIGITE O VALOR A SER SACADO: "))
                saque = Saque(valor_saque, conta)
                saque.registrar()

            else:
                print("USUÁRIO NÃO ENCONTRADO, TENTE CRIAR UM USUÁRIO E UMA CONTA PARA PODER SACAR.")

        
        if escolha == '3':
           ver_extrato(conta.saldo_valor, conta.historico.transacoes)


        elif escolha == '4':
            criar_usuario(clientes)
            print(clientes)
        

        elif escolha == '5':
            numero_contas = len(contas) + 1
            contas.append(Conta.nova_conta(numero_contas, clientes))


        elif escolha == '6':
            lista_contas(contas)

        
        elif escolha == '7':
            print("OBRIGADO POR USAR NOSSO SISTEMA!")
            break
        

        else:
            continue


main()