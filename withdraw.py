def withdraw(account:int,withdraw_amount:int)->str:
    curr_withdraw=users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} Withdraw successful and \n current balance is:{user[account]['balance']}"
    return "Insufficient Amount"