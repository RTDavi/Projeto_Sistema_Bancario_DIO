def depositar(saldo, valor_deposito, extrato, /):

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato['Depositos'].append(valor_deposito)

        print(f"\nVOCÊ DEPOSITOU R${valor_deposito:.2f}, SEU SALDO ATUAL É DE R${saldo:.2f}")

        return saldo
    

    else:
        print("\n NÃO É POSSÍVEL DEPOSITAR VALORES NEGATIVOS")

def sacar(*, saldo, valor_saque, extrato, limite_por_saque, numero_saques, limite_saques):

    if valor_saque > limite_por_saque:
        print("\n[NÃO FOI POSSÍVEL CONCLUIR A TRANSAÇÃO, LIMITE POR SAQUE EXCEDIDO.]")


    elif numero_saques >= limite_saques:
        print("\n[NÃO FOI POSSíVEL CONCLUIR A TRANSAÇÃO, LIMITE DE SAQUES DIARIOS EXCEDIDOS.]")


    elif saldo < valor_saque:
        print("\n[NÃO FOI POSSíVEL CONCLUIR A TRANSAÇÃO, SALDO INSUFICIENTE.]")
        

    else:
        saldo -= valor_saque
        numero_saques += 1
        print(f"\n[TRANSAÇÃO CONCLUÍDA, SALDO ATUAL É DE R${saldo:.2f}]")
        extrato['Saques'].append(valor_saque)

    return saldo

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
       
       if usuario["cpf"] == cpf:
            return True
       else:
           return False

def criar_conta(agencia, contas, usuarios, numero_conta):
    cpf = input("DIGITE NOVAMENTE SEU CPF:\n => ")
    nome_usuario = [nome['nome'] for nome in usuarios if cpf == nome['cpf']]

    if filtrar_cpf(cpf, usuarios) == True:
        contas.append({
            "Numero_conta" : numero_conta,
            "Agencia_Bancaria" : agencia,
            "Usuario" : nome_usuario
        })
        print("CONTA CRIADA COM SUCESSO!")
    else:
        print("CPF NÃO ENCONTRADO, CRIE UM USUÁRIO.")

def ver_extrato(saldo, /, *, extrato):
    deposito_contador = 0
    saque_contador = 0

    print("############## EXTRATO ##############")
    print("\nDEPÓSITOS:")
    for deposito in extrato['Depositos']:
        deposito_contador += 1
        print(f"DEPÓSITO {deposito_contador}: R${deposito:.2f}")
        

    print("\nSAQUES:")
    for saque in extrato['Saques']:
        saque_contador += 1
        print(f"SAQUE {saque_contador}: R${saque:.2f}")


    print(f"\nSALDO ATUAL: R${saldo:.2f}")
    print("#####################################")

def lista_contas(contas):
    contador = 0
    print("""############## CONTAS BANCARIAS ##############""")
    for conta in contas:
        contador += 1
        print(f"{contador}. {conta}")
    
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
   
    LIMITE_POR_SAQUE = 500
    LIMITE_SAQUES = 3
    NUMERO_AGENCIA = "0001"

    usuarios = []
    contas = []
    extrato = {'Depositos': [] , 'Saques': []}

    numero_saques = 0
    saldo = 0
    numero_contas = 0

    while True:
        escolha = menu_bancario()


        if escolha == '1':
            quantia_deposito = float(input("DIGITE A QUANTIA QUE DESEJA DEPOSITAR: "))
            saldo = depositar(saldo, quantia_deposito, extrato)


        elif escolha == '2':
            quantia_saque = float(input("DIGITE A QUANTIDADE (LIMITE DE R$500 POR SAQUE):"))
            saldo = sacar(
                saldo = saldo, 
                valor_saque = quantia_saque, 
                extrato = extrato,
                limite_por_saque = LIMITE_POR_SAQUE,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
                )
            numero_saques += len(extrato['Saques']) - 1
    
        
          
        elif escolha == '3':
           ver_extrato(saldo, extrato = extrato)


        elif escolha == '4':
            criar_usuario(usuarios)


        elif escolha == '5':
            numero_contas = len(contas) + 1
            criar_conta(NUMERO_AGENCIA, contas, usuarios, numero_contas)


        elif escolha == '6':
            lista_contas(contas)

        
        elif escolha == '7':
            print("OBRIGADO POR USAR NOSSO SISTEMA!")
            break
        

        else:
            print("\nESCOLHA INVÁLIDA, TENTE NOVAMENTE.")

main()