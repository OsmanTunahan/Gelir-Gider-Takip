from tkinter import ttk, messagebox
from services.expense_service import add_expense
from services.company_service import get_all_companies

class AddExpenseTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Tutar:").grid(row=0, column=0, padx=10, pady=10)
        self.expense_amount_entry = ttk.Entry(self)
        self.expense_amount_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self, text="Tarih (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
        self.expense_date_entry = ttk.Entry(self)
        self.expense_date_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self, text="Aciklama:").grid(row=2, column=0, padx=10, pady=10)
        self.expense_description_entry = ttk.Entry(self)
        self.expense_description_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self, text="Firma:").grid(row=3, column=0, padx=10, pady=10)
        self.company_combobox = ttk.Combobox(self)
        self.company_combobox['values'] = [company.name for company in get_all_companies()] + ["Diger"]
        self.company_combobox.grid(row=3, column=1, padx=10, pady=10)

        self.add_expense_button = ttk.Button(self, text="Ekle", command=self.add_expense)
        self.add_expense_button.grid(row=4, columnspan=2, padx=10, pady=10)

    def add_expense(self):
        amount = self.expense_amount_entry.get()
        date = self.expense_date_entry.get()
        description = self.expense_description_entry.get()
        company_name = self.company_combobox.get()

        if amount and date:
            if company_name == "Diger":
                company_id = None
            else:
                companies = get_all_companies()
                company = next((c for c in companies if c.name == company_name), None)
                company_id = company.id if company else None

            add_expense(float(amount), date, description, company_id)
            messagebox.showinfo("Success", "Gider basariyla eklendi!")
        else:
            messagebox.showerror("Error", "Lutfen miktari ve tarihi girin.")