import tkinter as tk
from tkinter import ttk
from app.utils.stats import calculate_monthly_statistics, calculate_company_expense_statistics
from app.services.company_service import get_all_companies

class StatisticsTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):
        self.statistics_text = tk.Text(self)
        self.statistics_text.pack(expand=1, fill='both')

        self.show_statistics_button = ttk.Button(self, text="Istatistikleri Goruntule", command=self.show_statistics)
        self.show_statistics_button.pack(padx=10, pady=10)

    def show_statistics(self):
        self.statistics_text.delete(1.0, tk.END)

        self.statistics_text.insert(tk.END, "Aylik Istatistik:\n")
        for stat in calculate_monthly_statistics():
            self.statistics_text.insert(tk.END, f"Ay: {stat[0]}, Income: {stat[1]}, Gider: {stat[2]}, Kâr/Zarar: {stat[3]}\n")

        self.statistics_text.insert(tk.END, "\nFirma Gider Istatistikleri:\n")
        for company, expense in calculate_company_expense_statistics().items():
            company_name = 'Diger' if company == 'Diger' else get_all_companies()[company-1].name
            self.statistics_text.insert(tk.END, f"Firma: {company_name}, Gider: {expense}\n")