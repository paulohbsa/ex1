
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual o Valor que desejas depositar: "))
        if (valor > 0):
            saldo += valor
            extrato += f"Depósito de: R${valor:.2f}\n"
            
        elif(valor <= 0):
            print("O valor deve ser maior que zero!")
        else:
            print("Deves digitar um número válido, cidadão...") 


    elif opcao == "s":
        saques_restantes = LIMITE_SAQUES - numero_saques
        valor = float(input(f"Qual o Valor que desejas saquear (saques sobrando {saques_restantes}): "))
        if ((valor > 0) and (valor <= saldo) and (valor <= limite) and (numero_saques < LIMITE_SAQUES)):
            saldo -= valor
            numero_saques += + 1
            extrato += f"Saque de: R${valor:.2f}\n"
            
        elif(valor<=0):
            print("O valor deve ser maior que zero!")
        elif(valor>saldo):
            print("O valor deve ser menor que vosso saldo!")
        elif(valor>limite):
            print(f"O valor deve ser menor que vosso limite de {limite}!")
        elif(numero_saques >= LIMITE_SAQUES):
            print(f"Já sacastes o numero máximo de vezes que é de {LIMITE_SAQUES}")
        else:
            print("Deves digitar um número válido, cidadão...")    
        
            

    elif opcao == "e":
        extrato_array = extrato.split()
        print("\n================ EXTRATO ================")
        print(extrato)
        print(f"Vosso saldo atual de vossa senhoria é de R${saldo}")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")