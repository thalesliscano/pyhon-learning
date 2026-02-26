class ContaBancaria:
    def __init__(self, titular:str, saldo:float):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor:float):
        if(valor <= 0):
            print("Por favor informe um valor maior que zero!")
        else:
            self.saldo += valor
    
    def sacar(self, valor:float) -> float:
        if(valor <= 0):
            print("Por favor informe um valor maior que zero!")
            self.sacar()
        if(valor > self.saldo):
            print("Saldo insuficiente para saque, por favor informe um valor que você possua em conta!")
        else:
            self.saldo -= valor
            return self.saldo

    def ver_saldo(self):
        print(f"Seu saldo em conta é...")
        print(f"Valor: R${self.saldo:.2f}")

