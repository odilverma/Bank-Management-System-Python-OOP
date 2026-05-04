#--------------BANK ACCOUNT CLASS----------------
class BankAccount:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def show_details(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")


#----------------LOAD ACCOUNTS FROM FILE---------------
accounts = []

try:
    with open("accounts.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            acc_no = int(data[0])
            name = data[1]
            balance = int(data[2])
            accounts.append(BankAccount(name, acc_no, balance))
except FileNotFoundError:
    pass


#---------------HELPER FUNCTIONS----------------
def find_account(account_no):
    for acc in accounts:
        if acc.account_no == account_no:
            return acc
    return None


def save_accounts():
    with open("accounts.txt", "w") as file:
        for acc in accounts:
            file.write(f"{acc.account_no},{acc.name},{acc.balance}\n")


def save_transaction(account_no, t_type, amount, balance):
    with open("transactions.txt", "a") as file:
        file.write(f"{account_no},{t_type},{amount},{balance}\n")


def show_transactions(account_no):
    print("\n--- Transaction History ---")
    found = False
    try:
        with open("transactions.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if int(data[0]) == account_no:
                    print(f"{data[1]} | Amount: {data[2]} | Balance: {data[3]}")
                    found = True
        if not found:
            print("No transactions found")
    except FileNotFoundError:
        print("Transaction file not found")


#----------------MAIN MENU----------------
while True:
    print("\n------ BANK MANAGEMENT SYSTEM ------")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Account Details")
    print("5. Show Transactions")
    print("6. Exit")

    choice = input("Enter choice: ")

    #CREATE ACCOUNT
    if choice == "1":
        name = input("Enter name: ")
        acc_no = int(input("Enter account number: "))
        balance = int(input("Enter initial balance: "))

        if find_account(acc_no):
            print("Account already exists")
        else:
            accounts.append(BankAccount(name, acc_no, balance))
            save_accounts()
            print("Account created successfully")

    #DEPOSIT
    elif choice == "2":
        acc_no = int(input("Enter account number: "))
        acc = find_account(acc_no)

        if acc:
            amount = int(input("Enter amount: "))
            if amount <= 0:
                print("Invalid amount")
            else:
                acc.deposit(amount)
                save_accounts()
                save_transaction(acc_no, "DEPOSIT", amount, acc.balance)
        else:
            print("Account not found")

    #WITHDRAW
    elif choice == "3":
        acc_no = int(input("Enter account number: "))
        acc = find_account(acc_no)

        if acc:
            amount = int(input("Enter amount: "))
            if amount <= 0:
                print("Invalid amount")
            else:
                acc.withdraw(amount)
                save_accounts()
                save_transaction(acc_no, "WITHDRAW", amount, acc.balance)
        else:
            print("Account not found")

    #SHOW DETAILS
    elif choice == "4":
        acc_no = int(input("Enter account number: "))
        acc = find_account(acc_no)

        if acc:
            acc.show_details()
        else:
            print("Account not found")

    #SHOW TRANSACTIONS
    elif choice == "5":
        acc_no = int(input("Enter account number: "))
        show_transactions(acc_no)

    #EXIT
    elif choice == "6":
        print("Thank you. Exiting program.")
        break

    else:
        print("Invalid choice")
            