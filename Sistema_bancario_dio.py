menu_bancario = """
   ############## BEM VINDO AO MENU BANCARIO ##############

   [1] DEPOSITAR
   [2] SACAR
   [3] VER EXTRATO
   [4] SAIR

   ########################################################

   ESCOLHA UMA OPÇÃO: """

saldo = 0
LIMITE_POR_SAQUE = 500
extrato = {'Depositos': [] , 'Saques': [] ,
           }
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    escolha = input(menu_bancario)


    if escolha == '1':
        quantia_deposito = float(input("DIGITE A QUANTIA QUE DESEJA DEPOSITAR: "))
        if quantia_deposito > 0:
            saldo += quantia_deposito
            extrato['Depositos'].append(quantia_deposito)

            print(f"\nVOCÊ DEPOSITOU R${quantia_deposito:.2f}, SEU SALDO ATUAL É DE R${saldo:.2f}")
    

        else:
            print("\n NÃO É POSSÍVEL DEPOSITAR VALORES NEGATIVOS")


    elif escolha == '2':
        quantia_saque = float(input("DIGITE A QUANTIDADE (LIMITE DE R$500 POR SAQUE):"))

        if quantia_saque > LIMITE_POR_SAQUE:
            print("\n[NÃO FOI POSSÍVEL CONCLUIR A TRANSAÇÃO, LIMITE POR SAQUE EXCEDIDO.]")


        elif numero_saques == LIMITE_SAQUES:
            print("\n[NÃO FOI POSSíVEL CONCLUIR A TRANSAÇÃO, LIMITE DE SAQUES DIARIOS EXCEDIDOS.]")


        elif saldo < quantia_saque:
            print("\n[NÃO FOI POSSíVEL CONCLUIR A TRANSAÇÃO, SALDO INSUFICIENTE.]")
        

        else:
            saldo -= quantia_saque
            numero_saques += 1

            print(f"\n[TRANSAÇÃO CONCLUÍDA, SALDO ATUAL É DE R${saldo:.2f}]")
            extrato['Saques'].append(quantia_saque)
        


    elif escolha == '3':
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


    elif escolha == '4':
        break


    else:
        print("\nESCOLHA INVÁLIDA, TENTE NOVAMENTE.")
