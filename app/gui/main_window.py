import tkinter as tk
from tkinter import ttk
from gui.add_company_tab import AddCompanyTab
from gui.add_income_tab import AddIncomeTab
from gui.add_expense_tab import AddExpenseTab
from gui.statistics_tab import StatisticsTab

class IncomeExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gelir-Gider Takip Otomasyonu")

        self.create_widgets()

    def create_widgets(self):
        self.tabs = ttk.Notebook(self.root)

        self.tab_add_company = AddCompanyTab(self.tabs)
        self.tab_add_income = AddIncomeTab(self.tabs)
        self.tab_add_expense = AddExpenseTab(self.tabs)
        self.tab_statistics = StatisticsTab(self.tabs)

        self.tabs.add(self.tab_add_company, text='Firma Ekle')
        self.tabs.add(self.tab_add_income, text='Gelir Ekle')
        self.tabs.add(self.tab_add_expense, text='Gider Ekle')
        self.tabs.add(self.tab_statistics, text='Istatistikler')

        self.tabs.pack(expand=1, fill='both')