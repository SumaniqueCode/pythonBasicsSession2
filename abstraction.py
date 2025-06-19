#Abstraction in python

from abc import ABC, abstractmethod

class Wallets(ABC):
    @abstractmethod
    def pay(self):
        pass

class Paypal(Wallets):
    def pay(self):
        print("Paypal payment successful")

class MasterCard(Wallets):
    def pay(self):
        print("MasterCard payment successful")

#displaying the abstract class
def displayData( wallet : Wallets, amount):
    print("This is a function to display data")
    wallet.pay()
    print("Amount to be paid is: ", amount)

displayData( Paypal(), 1000)

