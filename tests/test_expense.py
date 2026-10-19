import pytest


from expense_tracker.expense import Expense


def test_create_expense():
    expense = Expense(120, "午餐", "現金")

    assert expense.amount == 120
    assert expense.category == "午餐"
    assert expense.payment == "現金"


def test_negative_amount():
    with pytest.raises(
        ValueError,
        match = "金額不能是負數"
    ):
        Expense(-100, "午餐", "現金")

def test_invalid_amount_type():
    with pytest.raises(
        TypeError,
        match = "金額必須是整數"
    ):
        Expense(1.1, "午餐", "現金")

def test_bool_amount():
    with pytest.raises(
        TypeError,
        match = "金額必須是整數"
    ):
        Expense("True", "午餐", "現金")

def test_empty_category():
    with pytest.raises(
        ValueError,
        match = "項目不能是空白"
    ):
        Expense(120, "", "現金")

def test_whitespace_category():
    with pytest.raises(
        ValueError,
        match = "項目不能是空白"
    ):
        Expense(120, " ", "現金")

def test_category_is_stripped():
    expense = Expense(120, " 午餐 ", "現金")
    assert expense.category == "午餐"

def test_payment_correct():
    test1 = Expense(120, " 午餐 ", "現金")
    test2 = Expense(120, " 午餐 ", "刷卡")
    assert test1.payment == "現金"
    assert test2.payment == "刷卡"
    with pytest.raises(
            ValueError,
            match = "付款方式只能是現金或刷卡"
        ):
            Expense(120, "午餐", "Line Pay")
