class BankAccount:
    def __init__(self, no, saldo=0):
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")

        self.no = no
        self.saldo = saldo


Dimas = BankAccount("9876543", 250000)
print(f"Dimas ({Dimas.no}) saldo: {Dimas.saldo}")

try:
    Riko = BankAccount("7654321", -50000)
    print(f"Riko ({Riko.no}) saldo: {Riko.saldo}")

except ValueError as e:
    print(f"Riko tidak memiliki saldo ({e})")