from .storage import load_data, insert_expense, del_exp_from_db
from .utils import inputchk
from .expense_tracker import ExpenseTracker

def menu():
    print("""
        ======== Expense Tracker ========\n\n
        1. 新增支出\n
        2. 刪除支出\n
        3. 修改支出\n
        4. 查看所有支出\n
        5. 查看總支出\n
        6. 離開\n\n
        =================================  
        """
    )
    while True : 
        
        choose = inputchk("請選擇:")
        if 1 <= choose <= 6 :
            return choose
        print("請輸入 1~6!")


def main():
    
    tracker = ExpenseTracker(load_data())
    while True : 
        choose = menu()
        if choose == 1:
            expadd = tracker.add_expense()
            if expadd is None :
                continue
            insert_expense(expadd)
            tracker.expenses.append(expadd)

        elif choose == 2:            
            if not tracker.has_expenses():
                continue
            tracker.show_expenses()
            tracker.delete_expense()



        elif choose == 3:
            if not tracker.has_expenses():
                continue
            tracker.show_expenses()
            if tracker.update_expense(): 
                save_data(tracker.expenses)

        elif choose == 4:
            if not tracker.has_expenses():
                continue
            tracker.show_expenses()
            print("\n")

        elif choose == 5:
            print(f"總支出為 : {tracker.total}\n")

        elif choose == 6:
            break

if __name__ == "__main__":
    main()
