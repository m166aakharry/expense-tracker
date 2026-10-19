class Expense:
    def __init__(self, amount, category, payment, expid = None ):
        if expid is None :
            self.expid = None
        elif not isinstance(expid, int) or isinstance(expid, bool):
            raise TypeError("ID必須是整數")
        elif expid <= 0 :
            raise ValueError("ID必須是正整數")
        if not isinstance(amount, int) or isinstance(amount, bool):
            raise TypeError("金額必須是整數")
        if amount < 0 :
            raise ValueError("金額不能是負數")
        if not category.strip():
            raise ValueError("項目不能是空白")
        if payment not in ("現金", "刷卡"):
            raise ValueError("付款方式只能是現金或刷卡")
        
        self.expid = expid
        self.amount = amount
        self.category = category.strip()
        self.payment = payment

    @classmethod
    def from_dict(cls, expense):
        return cls(
            expense["amount"],
            expense["category"],
            expense["payment"],
            expense["expid"],
        )

#    def to_dict(self):
#        expense = {
#            "expid" : self.expid,
#            "amount" : self.amount,
#            "category" : self.category,
#            "payment" : self.payment
#        } 
#        return expense  