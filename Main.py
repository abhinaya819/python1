# Database
users = {
    1001: {
        "name": "Abhinaya",
        "email": "abhinayakatta2003@gmail.com",
        "balance": 5000,
        "password": "1001",
        "history": []
    },
    1002: {
        "name": "Abhi",
        "email": "abhinayakatta27@gmail.com",
        "balance": 1000,
        "password": "1002",
        "history": []
    }
}


# Register
def register(username, email, balance, password):
    account = max(users.keys()) + 1

    users[account] = {
        "name": username,
        "email": email,
        "balance": balance,
        "password": password,
        "history": [f"Initial Deposit: {balance}"]
    }

    return f"Registration Successful!\nYour Account Number is {account}"


# Login
def login(account, password):
    if account in users and users[account]["password"] == password:
        print("\nLogin Successful")
        return True
    print("Invalid Account Number or Password")
    return False


# Balance
def balance(account):
    print("Current Balance:", users[account]["balance"])


# Withdraw
def withdraw(account, amount):
    if amount <= users[account]["balance"]:
        users[account]["balance"] -= amount
        users[account]["history"].append(f"Withdraw: {amount}")
        print("Withdraw Successful")
        print("Current Balance:", users[account]["balance"])
    else:
        print("Insufficient Balance")


# Deposit
def deposit(account, amount):
    users[account]["balance"] += amount
    users[account]["history"].append(f"Deposit: {amount}")
    print("Deposit Successful")
    print("Current Balance:", users[account]["balance"])


# Transfer
def transfer(from_acc, to_acc, amount):
    if to_acc not in users:
        print("Receiver Account Not Found")
        return

    if users[from_acc]["balance"] >= amount:
        users[from_acc]["balance"] -= amount
        users[to_acc]["balance"] += amount

        users[from_acc]["history"].append(
            f"Transfer to {to_acc}: {amount}"
        )
        users[to_acc]["history"].append(
            f"Received from {from_acc}: {amount}"
        )

        print("Transfer Successful")
        print("Current Balance:", users[from_acc]["balance"])
    else:
        print("Insufficient Balance")


# Mini Statement
def ministatement(account):
    print("\n----- MINI STATEMENT -----")
    print("Account :", account)
    print("Name    :", users[account]["name"])
    print("Balance :", users[account]["balance"])
    print("Transactions:")

    if len(users[account]["history"]) == 0:
        print("No Transactions")
    else:
        for item in users[account]["history"]:
            print("-", item)


# Logout
def logout():
    print("Thank you for using Mini Bank.")


# Main Program
print("====== MINI BANK ======")
print("1. Login")
print("2. Register")

choice = int(input("Enter your choice: "))

if choice == 1:

    account = int(input("Enter Account Number: "))
    password = input("Enter Password: ")

    if login(account, password):

        while True:

            print("\n1. Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Mini Statement")
            print("6. Logout")

            option = int(input("Enter your choice: "))

            if option == 1:
                balance(account)

            elif option == 2:
                amt = int(input("Enter Withdraw Amount: "))
                withdraw(account, amt)

            elif option == 3:
                amt = int(input("Enter Deposit Amount: "))
                deposit(account, amt)

            elif option == 4:
                receiver = int(input("Enter Receiver Account Number: "))
                amt = int(input("Enter Transfer Amount: "))
                transfer(account, receiver, amt)

            elif option == 5:
                ministatement(account)

            elif option == 6:
                logout()
                break

            else:
                print("Invalid Choice")

elif choice == 2:

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    bal = int(input("Enter Initial Deposit: "))
    password = input("Enter Password: ")

    print(register(name, email, bal, password))

else:
    print("Invalid Choice")