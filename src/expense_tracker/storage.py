import os
import mariadb
from .expense import Expense

def load_data():
    connection = None
    cursor = None 
    try:    
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, amount, category, payment
            FROM expenses
            ORDER BY id
        """)
        expenses = []
        for row in cursor:
            try:
                expid = row[0]
                amount = row[1]
                category = row[2]
                payment = row[3]
                expense = Expense( amount, category, payment, expid)
                expenses.append(expense)
                
            except (KeyError, TypeError, ValueError) as error:
                    raise ValueError(
                        f"支出資料檔案格式錯誤 : {error}"
                    )from error 
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:    
            connection.close()
    return expenses

def insert_expense(expense):
    connection = None
    cursor = None 
    try:    
        connection = connect_db()
        cursor = connection.cursor()
        sql = """
            INSERT INTO expenses(amount, category, payment)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql,(
            expense.amount,
            expense.category,
            expense.payment
            ))
        connection.commit()
        expid = cursor.lastrowid
        expense.expid = expid
        return expense
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:    
            connection.close()
        
def del_exp_from_db(expid):
    connection = None
    cursor = None 
    try:    
        connection = connect_db()
        cursor = connection.cursor()    
        sql = """
        DELETE FROM expenses WHERE id = ?
        """ 
        cursor.execute(
            sql,
            (expid,)
        )
        rowcount = cursor.rowcount
        connection.commit()
        if rowcount == 1 :
            print("成功刪除一筆資料")
            return True
        else :
            print("沒有刪除資料")
            return False
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:    
            connection.close()
            
#    try:    
#            with open("expenses.json", "r", encoding="utf-8") as file:
#            expenses = json.load(file)
#    except FileNotFoundError:
#       return []
#    
#    except json.JSONDecodeError as error:
#        raise ValueError(
#            f"支出資料檔案格式錯誤 : {error}"
#        )from error
#    
#   expense_objects = []
#
#    for index,expense in enumerate(expenses, start = 1):
#        try:
#            expense_object = Expense.from_dict(expense)
#            expense_objects.append(expense_object)
#        except (KeyError, TypeError, ValueError) as error:
#            raise ValueError(
#               f"第 {index} 筆支出資料錯誤：{error}"
#                )from error
  

#def save_data(expenses):
#    saveexpenses = []
#    for expense in expenses:
#        saveexpenses.append(expense.to_dict())
#    with open("expenses.json", "w", encoding="utf-8") as file:
#        json.dump(saveexpenses, file, ensure_ascii=False, indent=4)


def connect_db():
    return mariadb.connect(
        host="127.0.0.1",
        port=3306,
        user="expense_app",
        password=os.environ["DB_PASSWORD"],
        database="expense_tracker",
        )
