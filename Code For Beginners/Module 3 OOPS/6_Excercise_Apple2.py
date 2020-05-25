class Account:
    account_num = None
    name = None
    balance = None

    def set_data(self, ac_num, name, bal):
        self.account_num = ac_num
        self.name = name
        self.balance = bal


class User(Account):

    def get_data(self):
        print("Account Holder Name = ", self.account_num, "\nNumber = ", self.name, "\nBalance = ", self.balance)


U = User()
U.set_data(15242967,"Abhi",23000)
U.get_data()