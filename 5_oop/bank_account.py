class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited")
        else:
            print(f"Cannot deposit negative amount.")
        print(f"Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Amount withdrawn")
            else:
                print(f"Insufficient funds")
        else:
            print(f"Enter amount to withdraw.")
        print(f"Balance: {self.balance}")

    def __str__(self):
        to_string = "Account owner:\t\t" + self.owner \
                    + "\nAccount balance:\t" + str(self.balance)
        return to_string


if __name__ == '__main__':
    ac = Account('Vik', 100)
    print(ac)

    print(ac.owner)
    print(ac.balance)
    ac.deposit(int(input(f"Enter Amount to deposit: ")))
    ac.withdraw(int(input(f"Enter Amount to withdraw: ")))
    ac.withdraw(int(input(f"Enter Amount to withdraw: ")))

