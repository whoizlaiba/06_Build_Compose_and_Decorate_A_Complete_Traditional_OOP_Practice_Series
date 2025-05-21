# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Bank Alfalah"  

    def __init__(self):
        pass  

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"The New Bank Name is: {cls.bank_name}")

p1 = Bank()
p2 = Bank()

Bank.change_bank_name("Habib Metro")

print(p1.bank_name)
print(p2.bank_name)
print(Bank.bank_name)
