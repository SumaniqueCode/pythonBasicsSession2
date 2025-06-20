#Abstraction in python

from abc import ABC, abstractmethod

class Wallets(ABC):
    def pay(self,amount):
        pass

class Paypal(Wallets):
    def pay(self,):
        print("Paypal payment successful")
