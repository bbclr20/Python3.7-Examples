class Account:

    def __init__(self, name:str, id: str, balance: float) -> None: 
        self.__name = name
        self.__id = id
        self.__balance = balance

    def __str__(self):
        return f"{self.__name}, {self.__id}, {self.__balance}"

    # getter
    @property 
    def name(self) -> str:
        return self.__name

    @property
    def id(self) -> str:
        return self.__id

    @property
    def balance(self) -> float:
        return self.__balance

    # setter
    @name.setter
    def name(self, name: str):
        self.__name = name

    @id.setter
    def id(self, id: str):
        self.__id = id

    @balance.setter
    def balance(self, balance: float) -> float:
        self.__balance = balance

    # methods
    def deposit(self, amount: float):
        if amount <= 0:
            print("amount must greater than zero")
        else:
            self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    # static method
    @staticmethod
    def info():
        print("An account in the bank")

    # class method
    @classmethod 
    def default(cls):
        return cls("Guest", "00000", 100)
