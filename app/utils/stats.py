from app.services.income_service import get_all_income
from app.services.expense_service import get_all_expenses

def calculate_monthly_statistics():
    incomes = get_all_income()
    expenses = get_all_expenses()
    
    income_by_month = {}
    expense_by_month = {}

    for income in incomes:
        month = income.date[:7]  # YYYY-MM-DD
        income_by_month[month] = income_by_month.get(month, 0) + income.amount

    for expense in expenses:
        month = expense.date[:7]  # YYYY-MM-DD
        expense_by_month[month] = expense_by_month.get(month, 0) + expense.amount

    stats = []
    all_months = sorted(set(income_by_month.keys()).union(expense_by_month.keys()))

    for month in all_months:
        income = income_by_month.get(month, 0)
        expense = expense_by_month.get(month, 0)
        profit_loss = income - expense
        stats.append((month, income, expense, profit_loss))

    return stats

def calculate_company_expense_statistics():
    expenses = get_all_expenses()
    company_expense = {}

    for expense in expenses:
        company_id = expense.company_id or 'Diger'
        company_expense[company_id] = company_expense.get(company_id, 0) + expense.amount

    return company_expense