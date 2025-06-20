#Abstraction in python

from abc import ABC, abstractmethod

class Wallets(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class Paypal(Wallets):
    def pay(self,amount):
        print(f"\nPaypal payment successful with amount {amount} via paypal")

class Khalti(Wallets):
    def pay(self,amount):
        print(f"\nKhalti payment successful with amount {amount} via khalti")

def payment(wallet: Wallets, amount):
    wallet.pay(amount)
    
wallet = input("Enter wallet name: ")
amount = float(input("Enter amount to be paid: "))

if wallet.lower() == "paypal":
    payment(Paypal(), amount)
elif wallet.lower() == "khalti":
    payment(Khalti(), amount)
else:
    print("\nInvalid wallet name")