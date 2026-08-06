from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")
class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} in Cash.")
credit = CreditCardPayment()
upi = UPIPayment()
cash = CashPayment()
credit.pay(5000)
upi.pay(1500)
cash.pay(800)
