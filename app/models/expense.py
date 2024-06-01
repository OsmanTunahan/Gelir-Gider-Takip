class Expense:
    def __init__(self, id, amount, date, description, company_id=None):
        self.id = id
        self.amount = amount
        self.date = date
        self.description = description
        self.company_id = company_id

    def __repr__(self):
        return f"Expense(id={self.id}, amount={self.amount}, date='{self.date}', description='{self.description}', company_id={self.company_id})"