class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 
        
    
    
    def sum(self) -> int:
        '''Calcula a soma de dois números'''
        soma = self.num1 + self.num2
        return soma

    def sub(self) -> int:
        '''Calcula a subtração de 2 números'''
        subtraction = self.num1 - self.num2
        return subtraction

    def mult(self) -> int:
        '''Calcula a multiplicação de 2 números'''
        multiplication = self.num1 * self.num2
        return multiplication

    def div(self) -> int:
        '''Calcula a divisão de 2 números'''
        division = self.num1 / self.num2
        return division

if __name__ == "__name__":
    nova_calculadora = Calculadora()
    
    print(nova_calculadora.somar(1,2))