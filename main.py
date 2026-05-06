
# 3-m
class BankAccount:
    def __init__(self, owner, balnce, pin):
        self.owner = owner
        self._balance = balnce
        self.__pin = pin

    def deposit(self):
        print(f"Owner: {self.owner}")

    def withdraw(self):
        print(f"Wrong pin: {self.__pin}")

    def check_balance(self, x):
        self._balance += x

b1 = BankAccount(150, 20, "Wrong")
b1.deposit()
b1.withdraw()
b1.check_balance(30)


# # 4-m
class Phone:
    def __init__(self, model, battery, imei):
        self.model = model
        self._battery = battery
        self.__imei = imei

    def call(self, minutes):
        self._battery -= minutes

    def charge(self, x):
        self._battery += x

    def info(self):
        print(f"Model: {self.model}")
        print(f"Batareya: {self._battery}%")
        print(f"IMEI: {self.__imei}")


p1 = Phone("Samsung A15", 50, "987654321")

p1.call(20)
p1.charge(30)
p1.info()
