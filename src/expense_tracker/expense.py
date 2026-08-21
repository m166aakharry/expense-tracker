class Expense:
    def __init__(self, amount, category, payment):
        if not isinstance(amount, int) or isinstance(amount, bool):
            raise TypeError("金額必須是整數")
        if amount < 0 :
            raise ValueError("金額不能是負數")
        if not category.strip():
            raise ValueError("項目不能是空白")
        if payment not in ("現金", "刷卡"):
            raise ValueError("付款方式只能是現金或刷卡")

        self.amount = amount
        self.category = category.strip()
        self.payment = payment

    @classmethod
    def from_dict(cls, expense):
        return cls(
            expense["amount"],
            expense["category"],
            expense["payment"]
        )

    def to_dict(self):
        expense = {
            "amount" : self.amount,
            "category" : self.category,
            "payment" : self.payment
        } 
        return expense  