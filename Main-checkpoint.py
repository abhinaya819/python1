#Data Base
"""
users = {
             Account:{
                        'name':Username,
                        'email':user email,
                         'balance':5000,
                         'password':password
                     }
        }
"""

users = {
    1001:{'name':"Abhinaya",'email':'abhinayakatta2003@gmail.com','balance':5000,'password':'1001'},
    1002:{'name':"Abhi",'email':'abhinayakatta27@gmail.com','balance':1000,'password':'1002'},
     }
     
#Register function
def register(username:str,email:str,balance:int,password:str)->str:
    return "Register page under development process"

#Login function
def login(account:int,password:str)->bool:
    if account in users:
        if users[account]['password']==password:
            return True
        return False
    return False
    

# get balance
def balance(account:int)->str:
    curr_balance=users[account]['balance']
    return f"Current Balance is:{curr_balance}"
    

# withdraw
def withdraw(account:int,withdraw_amount:int)->str:
    curr_withdraw=users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} Withdraw successful and \n current balance is:{user[account]['balance']}"
    return "Insufficient Amount"
    
    # deposit
def deposit(account, deposit_amount:int)->str:
    user[account]['balance']+=deposit_amount
    return f"{deposit_amount} deposit successful and \n current balance is:{user[account]['balance']}"
    
    

#transfer function
def transfer(from_acc:int,to_acc:int,transfer_amount:int):
    print("user in transfer page")

# Ministatement function
def Ministatement(account:int):
    print("user in Ministatement page")

#logout
def logout():
    print("This is mini block,see you later")
    exit()

#main
if __name__ == "__main__":
    print("Welcome to the Mini Bank")
    print("1. Login \n 2. Register")
    choice=int(input("Enter your choice"))
    if choice == 1:
        #call login function
        account=int(input("Enter your account Number:"))
        password = input("Enter your Password:")
        login_val=login(account=account,password=password)
        while login_val:

            print("1. Get Balance \n 2. Withdraw \n 3. Deposit \n 4. Transfer \n 5. Ministatement \n 6. Logout")
            choice=int(input("Enter your choice:"))
            if choice == 1:
                #call Balance Functions 
                balance(account=account)
            elif choice == 2:
                #call Withdraw function
                amount=int(input("Enter your withdraw amount:"))
                print(withdraw(account=account,withdraw_amount=amount))
            elif choice == 3:
                #call deposit function
                amount=int(input("Enter your Deposit amount:"))
                print(Deposit(account=account,deposit_amount=amount))
            
            elif choice==4:
                receiver=int(input("Enter Receiver account number:"))
                amount=input("Enter your Transfer amount:")
                print(Transfer(from_account=account,to_acc=receiver,Transfer_amount=amount))

            elif choice==5:
                print(Ministatement(from_account=account))
            
            elif choice==6:
                priint(logout())
            else:
                print("Select your choice in between 1-6")
    elif choice==2:
        #call register function
        username=input("Enter your Name:")
        email=input("Enter your email id:")
        initial_deposit=int(input("Enter the initial deposit amount:"))            
        password = input("Enter your Password:")
        print(register(username=username,email=email,balance=initial_deposit,password=password))
    else:
        print("Invalid choice \n please select your choice from 1 and 2")

                
                