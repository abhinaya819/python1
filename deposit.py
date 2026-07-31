def deposit(account, deposit_amount:int)->str:
    user[account]['balance']+=deposit_amount
    return f"{deposit_amount} deposit successful and \n current balance is:{user[account]['balance']}"
    
    
