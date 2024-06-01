from tkinter import ttk, messagebox
from services.income_service import add_income

class AddIncomeTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Tutar:").grid(row=0, column=0, padx=10, pady=10)
        self.income_amount_entry = ttk.Entry(self)
        self.income_amount_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self, text="Tarih (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
        self.income_date_entry = ttk.Entry(self)
        self.income_date_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self, text="Aciklama:").grid(row=2, column=0, padx=10, pady=10)
        self.income_description_entry = ttk.Entry(self)
        self.income_description_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_income_button = ttk.Button(self, text="Ekle", command=self.add_income)
        self.add_income_button.grid(row=3, columnspan=2, padx=10, pady=10)

    def add_income(self):
        amount = self.income_amount_entry.get()
        date = self.income_date_entry.get()
        description = self.income_description_entry.get()
        if amount and date:
            add_income(float(amount), date, description)
            messagebox.showinfo("Success", "Gelir basariyla eklendi!")
        else:
            messagebox.showerror("Error", "Lutfen miktari ve tarihi girin.")