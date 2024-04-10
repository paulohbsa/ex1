
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[cu] Criar Usuario
[cc] Criar Conta
[q] Sair

=> """



def depositar(saldo, valor, extrato, /):
        
        if (valor > 0):
            saldo += valor
            extrato += f"Depósito de: R${valor:.2f}\n"
            
        elif(valor <= 0):
            print("O valor deve ser maior que zero!")
        else:
            print("Deves digitar um número válido, cidadão...") 
        return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if ((valor > 0) and (valor <= saldo) and (valor <= limite) and (numero_saques < limite_saques)):
        saldo -= valor
        numero_saques += + 1
        extrato += f"Saque de: R${valor:.2f}\n"
        
    elif(valor<=0):
        print("O valor deve ser maior que zero!")
    elif(valor>saldo):
        print("O valor deve ser menor que vosso saldo!")
    elif(valor>limite):
        print(f"O valor deve ser menor que vosso limite de {limite}!")
    elif(numero_saques >= limite_saques):
        print(f"Já sacastes o numero máximo de vezes que é de {limite_saques}")
    else:
        print("Deves digitar um número válido, cidadão...")    
        
    return saldo, extrato
    
        


def exibir_extrato(saldo, /, *, extrato):
    if(saldo <= 0):
        print("Vossa senhoria não tem saldo!")
    else:
        extrato_array = extrato.split()
        print("\n================ EXTRATO ================")
        print(extrato)
        print(f"Vosso saldo atual de vossa senhoria é de R${saldo}")


def criar_user(users):
    
    
    nome = input("digite o Nome ").lower()
    nascimento = input("digite data de nascimento ")
    cpf = input("digite o CPF ")
    for user in users:
        for i in user:
            if (cpf == i):
                print(f"usuário com o CPF {i} já existe")
                return
    
    logadouro = input("digite o logadouro  da residencia ")
    numero = input("digite o numero da residencia ")
    bairro = input("digite o bairro da residencia ")
    cidade = input("digite a cidade da residencia ")
    cigla = input("digite a cigla do estado da residencia ")
    
    end = logadouro + ", " + numero + " - " + bairro + " - " + cidade + "/" + cigla.upper()

    actUser = [nome.title(), nascimento, cpf, end]
    users.append({"nome": nome.title(), "nascimento": nascimento, "cpf": cpf, "endereco": end })
    

def print_users(users):
    for index, user in enumerate(users):
        print(f"\n{user}")

def print_contas(contas):
    for index, conta in enumerate(contas):
        print(f"\n{conta}")
        
        
def filtrar_user(cpf, users):
    usuarios_filtrados = [user for user in users if user["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, users):
    cpf = input("digite CPF do caboclo ")     
    user = filtrar_user(cpf, users)
    
    if user:
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": user}
    
    print("Usuario inesistente, sorry.")
    

def main():       
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    
    
    
    users = []
    contas = []
    
    
    
    while True:
        
        opcao = input(menu)
        
        if opcao == "d":
            valor = float(input("Qual o Valor que desejas depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            saques_restantes = LIMITE_SAQUES - numero_saques
            valor = float(input(f"Qual o Valor que desejas saquear (saques sobrando {saques_restantes}): "))
            saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)
            
        elif opcao == "e":
            print(f"saldo {saldo}")
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "cu":
            criar_user(users)
        
        elif opcao == "pu":
            print_users(users)
            
        elif opcao == "pc":
            print_contas(contas)
        
        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, users)
            if conta:
                contas.append(conta)    
        
            
        elif opcao == "z":
            print(f"saldo {saldo}")
            
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            


main()