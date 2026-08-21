from .utils import input_new_expense, input_expenses_index, inputchk, confirm
from .expense import Expense

class ExpenseTracker:
    def __init__(self,expenses):
        self._expenses = expenses
    
    @property
    def expenses(self):
        return self._expenses
    
    @expenses.setter
    def expenses(self, value):
        if not isinstance(value, list):
            raise TypeError("expenses 必須是 list")
        self._expenses = value

    @property
    def total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

    def show_expenses(self):
        print("\n=====今日支出=====")
        for index,expense in enumerate(self.expenses, start=1):
            print(
                f'{index}.'
                f'{expense.category}:'
                f'{expense.amount}元'
                f'使用{expense.payment}'
            )
    
    def add_expense(self):
        #取得資料
        expense = input_new_expense()
        #存入資料庫
        if confirm("確定要增加嗎?Y/N:"):    
            self.expenses.append(expense)
            return True
        return False
    
    def delete_expense(self):
        index = input_expenses_index("請輸入要刪除的項目編號:",self.expenses)
        if confirm("確定要刪除嗎?Y/N:"):
            self.expenses.pop(index)
            return True
        return False


    def update_expense(self):
        index = input_expenses_index("請輸入要修改的支出編號:",self.expenses)
        new_amount = inputchk("請輸入正確的金額:")
        if confirm("確定要修改嗎?Y/N:"):
            self.expenses[index].amount = new_amount
            return True
        return False
    
    def has_expenses(self):
        if len(self.expenses) == 0:
            print("目前沒有任何支出")
            return False
        
        return True
    