from datetime import datetime


class Wallet:

    def __init__(self):
        self.balance = 0
        self.blocked_users = []
        self.counter = {}
        self.transactions = []


    def pay(self, amount, name, shop, time):

        for names in self.blocked_users:
            if names == name:
                print("You are blocked by dad to use the wallet")
                return

        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print(f"The amount of {self.amount} has been paid")
            print("The remaining balance in the wallet is:")
            print(self.balance)
            t = [f"{name}, {shop}, {time}"]
            self.transactions.append(t)

            return
        elif amount > self.balance:
            print(f"Insufficient balance. The available balance is {self.balance}")
            # print(self.balance)
            return
        elif amount < 0:
            print("Enter Valid amount to be paid")
            return

    def add_money(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print(f"The amount {self.amount} has been added successfully")
        print(f"The final balance is {self.balance}")

    def withdraw_money(self, amount):
        self.amount = amount
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"The amount {self.amount} has been withdrawed successfully")
            print(f"The final balance is {self.balance}")
        else:
            print("Not enough balance to withdraw")

    def transactions_print(self):
        print(self.transactions)


class Dad(Wallet):

    def __init__(self):
        # self.blocklist = []
        self.requests_depositmoney = []
        self.request_paymorethanone = []
        self.system_request = []

    # def block_user(self, name):
    # self.blocklist.append(name)

    def receive_requests(self, name, type):
        self.name = name
        if type == 2:
            self.request_paymorethanone.append(f"{self.name} has requested to pay more than once")
        if type == 3:
            self.requests_depositmoney.append(f"{self.name} has requested to deposit money")
            return

    def system_requests(self):
        self.system_request.append("Wallet balance is less than $100")

    def print_requests(self):
        print("Requests to deposit money:")
        print(self.requests_depositmoney)
        print("System Notifications: ")
        print(self.system_request)

    def block_user(self, name):
        wallet_object.blocked_users.append(name)

    def approve_requests(self):
        pass


class Mom(Wallet):

    def __init__(self):
        self.requests = []
        self.system_request = []

    def receive_requests(self, name, type):
        self.name = name
        if type == 1:
            print(self.name)
            self.requests.append(f"{self.name} has requested to overpay")
            return
        elif type == 2:
            self.requests.append(f"{self.name} has requested to pay more than once")
            return

        elif type == 3:
            self.requests.append(f"{self.name} has requested to deposit money")
            return

    def system_requests(self):
        self.system_request.append("Wallet balance is less than $100")

    def print_requests(self):
        print("Requests to be approve:")
        print(self.requests)
        print("System Notifications: ")
        print(self.system_request)

    def approve_requests(self):
        pass


class Children(Wallet):  # inherited wallet so balance can be used   #counter to be implemented

    # pay = Wallet()
    def __init__(self):
        pass

    def pay(self, amount, name, shop, time):
        if amount <= 50:
            wallet_object.pay(amount, name, shop, time)
        elif amount > 50:
            print("You cannot pay more than $50")
            print("Request parents to do so")
            return

class Notifications(Wallet):
    dad = Dad()
    mom = Mom()

    def __init__(self):
        pass

    def send_message(self, name, type):
        if type == 1:  # Overpay
            mom.receive_requests(name, type)
        elif type == 2:  # More than once
            dad.receive_requests(name, type)
            mom.receive_requests(name, type)
        elif type == 3:  # Balance is 0
            dad.receive_requests(name, type)
            mom.receive_requests(name, type)

    def system_notifications(self):

        if self.balance < 100:
            self.name = "Wallet"
            dad.system_requests()
            mom.system_requests()

class FamilyMembers():

    def __init__(self):
        self.members = 10
        self.family_members_name = ["Dad", "Mom", "C1", "C2", "C3", "C4", "C5", "Ch6", "Child 7", "Child 8"]

    def login(self, name):
        for names in self.family_members_name:
            if names == name:
                return True

        return False


if __name__ == "__main__":

    family_bansal = FamilyMembers()
    wallet_object = Wallet()
    notification_object = Notifications()
    dad = Dad()
    mom = Mom()
    children = Children()

    while True:

        print("Welcome to the Family Wallet")
        print("1.Login")

        name = input("Enter Name: ")
        type = str(input("Enter D for Dad, M for Mom and C for Children: "))
        loggedin = family_bansal.login(name)

        if loggedin == True:

            while True:
                print("1.Pay from Wallet")
                print("2.Add money to the wallet")
                print("3.Withdraw money from the wallet")
                print("4.View Transactions")
                print("5.Block the user")
                print("6.Make a request")
                print("7.Approve a request")
                print("8.Logout")
                login_choice = int(input())

                if login_choice == 1:

                    amount = int(input("Enter the amount to be paid: "))
                    shop = str(input("Enter the shop where to pay"))
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                    if type == "D" or type == "M":
                        wallet_object.pay(amount, name, shop, dt_string)
                    elif type == "C":
                        children.pay(amount, name, shop, dt_string)

                    print("\n1.Back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                if login_choice == 2:
                    if type == "D" or type == "M":

                        amount = int(input("Enter the amount you want to add: "))
                        if amount > 0:
                            wallet_object.add_money(amount)
                        else:
                            print("Enter the valid amount")
                    else:
                        print("Children cannot add money")

                    print("\n1.Back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                if login_choice == 3:
                    if type == "D" or type == "M":

                        amount = int(input("Enter the amount you want to withdraw: "))
                        if amount > 0:
                            wallet_object.withdraw_money(amount)
                        else:
                            print("Enter the valid amount")
                    else:
                        print("Children cannot withdraw money")

                    print("\n1.Back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                if login_choice == 4:
                    if type == "D" or type == "M":
                        wallet_object.transactions_print()
                    else:
                        print("Children cannot view the transactions")

                    print("\n1.Back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                if login_choice == 5:
                    if type == "D":
                        name = str(input("Enter the name whom you want to block: "))
                        dad.block_user(name)
                    else:
                        print("Dad only has authority to block someone")

                if login_choice == 6:

                    if type == "C":
                        print("1. Want to overpay")
                        print("2. Want to pay more than once")
                        print("3. Want to request to add money")

                        choice = int(input("Enter the type of request you want to make"))
                        notification_object.send_message(name, choice)

                    else:
                        print("Parents are not allowed to make requests")

                    print("\n1.Back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                if login_choice == 7:
                    if type == "D":
                        dad.print_requests()
                    elif type == "M":
                        mom.print_requests()
                    else:
                        print("Children cannot approve requests")

                    print("\n1.Back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                if login_choice == 8:
                    break

        elif loggedin == False:
            print("Invalid credentials")