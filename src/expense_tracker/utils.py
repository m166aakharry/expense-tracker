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
        
def input_expenses_index(message,expenses):
    index = inputchk(message)
    while True:
        if 0 < index <= len(expenses):
            return index-1
        index = inputchk("輸入錯誤，請輸入小於已有的編號！")

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