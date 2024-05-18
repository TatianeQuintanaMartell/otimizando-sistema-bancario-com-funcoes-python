class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_realizados = 0  
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def sacar(self, valor):
        if self.saques_realizados >= 3:
            print("Você já realizou o número máximo de 3 saques hoje.")
            return       

        if valor > 0:
            if valor > 500:
                print("O valor do saque não pode ser maior que R$500.")
                return
        
            if valor <= self.saldo:
                self.saldo -= valor
                self.extrato.append(f"Saque: -R${valor:.2f}")
                self.saques_realizados += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")
    
    def ver_extrato(self):
        print("\nExtrato da Conta:")
        for item in self.extrato:
            print(item)
        print(f"Saldo atual: R${self.saldo:.2f}\n")

def main():
    conta = Banco()
    
    while True:
        print("Bem-vindo ao Banco")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor para depositar: R$"))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor para sacar: R$"))
            conta.sacar(valor)
        elif opcao == '3':
            conta.ver_extrato()
        elif opcao == '4':
            print("Obrigado por usar o Banco. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        print()

if __name__ == "__main__":
    main()
