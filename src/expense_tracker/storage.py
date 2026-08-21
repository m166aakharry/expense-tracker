import json
from .expense import Expense

def load_data():
    try:    
        with open("expenses.json", "r", encoding="utf-8") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError as error:
        raise ValueError(
            f"支出資料檔案格式錯誤 : {error}"
        )from error
    
    expense_objects = []

    for index,expense in enumerate(expenses, start = 1):
        try:
            expense_object = Expense.from_dict(expense)
            expense_objects.append(expense_object)
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(
                f"第 {index} 筆支出資料錯誤：{error}"
                )from error
        
    return expense_objects

def save_data(expenses):
    saveexpenses = []
    for expense in expenses:
        saveexpenses.append(expense.to_dict())
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(saveexpenses, file, ensure_ascii=False, indent=4)
