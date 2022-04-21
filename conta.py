from cmath import isnan


class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000):
        print('Construindo objeto ... {}'.format(self))
        self.__numero = numero # __ means private
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Conta: {}'.format(self.__numero))
        print('Titular: {}'.format(self.__titular))
        print('Saldo: R${:.2f}'.format(self.__saldo))

    def deposita(self, valor):
        if(not isnan(valor) and valor > 0):
            self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        saque_maximo = self.__saldo + self.__limite
        return valor_a_sacar <= saque_maximo

    def saca(self, valor):
        if(not isnan(valor) and valor > 0):
            if(self.__pode_sacar(valor)):
                self.__saldo -= valor
            else:
                print('Não existe limite para um saque de R${:.2f}'.format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # def get_saldo(self):
    #     return self.__saldo

    # def get_titular(self):
    #     return self.__titular
    
    # def get_limite(self):
    #     return self.__limite
    
    # def set_limite(self, limite):
    #     self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {
                '001': 'Banco do Brasil',
                '104': 'Caixa Econômica Federal',
                '237': 'Bradesco'
            }

    @staticmethod
    def codigo_banco():
        # return '001' + ': ' + Conta.codigos_bancos().get('001')
        return '001'