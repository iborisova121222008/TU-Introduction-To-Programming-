from errors import InvalidAccountType, InvalidAccountData

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT", "PAYMENT")

    def __init__(self, iban, currency, type) -> None:
        if type not in self.ACC_TYPES:
            raise InvalidAccountType()

        try:
            currency = int(currency)
        except:
            raise InvalidAccountData()

        self.iban = iban
        self.currency = currency
        self.type = type


    def print(self):
        print(f"{self.iban}: {self.currency}, {self.type}")
