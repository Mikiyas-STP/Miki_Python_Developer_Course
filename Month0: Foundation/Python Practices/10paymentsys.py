class Payment:
    def __init__(self, amount: float):
        self.amount = amount

    def process(self) -> str:
        return f"Processing {self.amount}..."

class CreditCardPayment(Payment):
    # 1. Take BOTH amount (for parent) and card (for self)
    def __init__(self, amount: float, card_number: str):
        # 2. Hand the amount to the parent
        super().__init__(amount) 
        # 3. Keep the card_number
        self.card_number = card_number

    # 4. OVERRIDE the parent method
    def process(self) -> str:
        return f"Processing {self.amount} via Credit Card {self.card_number}..."

class PayPalPayment(Payment):
    def __init__(self, amount: float, email: str):
        super().__init__(amount)
        self.email = email

    def process(self) -> str:
        return f"Processing {self.amount} via PayPal account {self.email}..."

if __name__ == "__main__":
    payments = [
        CreditCardPayment(100.50, "1234-5678"),
        PayPalPayment(50.00, "user@test.com")
    ]
    
    # Standard loop for printing backend results
    for p in payments:
        print(p.process())

#I asked: If I have p = CreditCardPayment(100, "123"), will isinstance(p, Payment) be True?
#The Answer: True.
#Because CreditCardPayment inherits from Payment, it "is a" type of Payment. This is very useful in backend development because you can write a function that accepts a Payment object, and it will work perfectly whether you pass it a Credit Card, PayPal, or Crypto payment!
# | Concept                   | Summary                                                                                                                  |
# | ------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
# | Polymorphism in your code | Both `CreditCardPayment` and `PayPalPayment` implement `process()`, but each returns a different result.                 |
# | Why your loop works       | The loop calls `p.process()` on each object, and Python automatically uses the correct version based on the object type. |
