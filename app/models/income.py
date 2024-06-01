class Income:
    def __init__(self, id, amount, date, description):
        self.id = id
        self.amount = amount
        self.date = date
        self.description = description

    def __repr__(self):
        return f"Income(id={self.id}, amount={self.amount}, date='{self.date}', description='{self.description}')"