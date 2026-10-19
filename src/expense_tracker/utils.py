from .expense import Expense

def payment_type():
    while True:
        keyin = inputchk("現金請輸入1,刷卡請輸入2:")
        if keyin == 1:
            return "現金"
        elif keyin == 2:
            return "刷卡"
        print("輸入錯誤，現金請輸入1，刷卡請輸入2:")

def inputchk(message):
    while True:
        try:
            keyin = int(input(message))
            return keyin
        except ValueError:
            print("輸入錯誤，請重新輸入數字！")
        
def input_expid(message):
    expid = inputchk(message)
    return expid

def find_exp_by_id(expid, expenses):
    while True:
        for expense in expenses:
            if expense.expid == expid:
                return expense
        expid = input_expid("請輸入已存在的編號：")
        
    

def confirm(message):
    while True:
        check = input(message).upper()
        if check == "Y":
            return True
        elif check == "N":
            return False
        else:
            print ("請重新輸入:")

def input_new_expense():
        amount = inputchk(f"請輸入金額:")
        category = input(f"請輸入項目:")
        payment = payment_type()
        return Expense(amount, category, payment)