def menu():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    opcao = 0
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        print("\nEscolha uma opcao\n")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Criar Cliente Banco")
        print("5. Criar Conta Corrente")
        print("6. Sair\n")        
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor para depositar: R$"))
            saldo, extrato = depositar(valor, saldo, extrato)
        elif opcao == '2':
            valor = float(input("Digite o valor para sacar: R$"))
            saldo, extrato, numero_saques = sacar(valor=valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, limite=limite)
        elif opcao == '3':
            imprimir_extrato(extrato, saldo)
        elif opcao == '4':
            criar_cliente_banco(usuarios)
        elif opcao == '5':
            criar_conta_corrente(contas, usuarios)    
        elif opcao == '6':
            print("Obrigado por usar o Banco. Até logo!\n")
            break
        else:
            print("Opção inválida. Tente novamente.")

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n"
        print("Deposito realizado com sucesso")           
    else:
        print("So é possível depositar valores positivos na conta bancaria") 

    return saldo, extrato       

def sacar(*, valor, saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diários atingido.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite:
        print(f"O valor do saque excede o limite de R${limite:.2f} por saque.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Só é possível sacar valores positivos.")

    return saldo, extrato, numero_saques

def criar_cliente_banco(usuarios):
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF do cliente: ")
    endereco = input("Digite o endereço (logradouro, numero, bairro, cidade, estado sigla): ")
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return
    
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    
    print("Cliente cadastrado com sucesso!")

def criar_conta_corrente(contas, usuarios):
    if not usuarios:
        print("Não existem clientes cadastrados.")
        return

    cpf = input("Digite o CPF do cliente para associar a conta: ")
    cliente_encontrado = False
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            cliente_encontrado = True
            break
    
    if not cliente_encontrado:
        print("Cliente não encontrado.")
        return
    
    numero_conta = len(contas) + 1
    contas.append({
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    })

    print(f"Conta corrente criada com sucesso para o cliente {usuario['nome']}, número da conta: {numero_conta}")

def imprimir_extrato(extrato, saldo):
    print("\nExtrato:")
    print(extrato)
    print(f"Saldo atual: R${saldo:.2f}")


menu()