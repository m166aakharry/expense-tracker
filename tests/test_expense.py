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