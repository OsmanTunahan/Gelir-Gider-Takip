from tkinter import ttk, messagebox
from services.company_service import add_company

class AddCompanyTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Firma Adi:").grid(row=0, column=0, padx=10, pady=10)
        self.company_name_entry = ttk.Entry(self)
        self.company_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_company_button = ttk.Button(self, text="Ekle", command=self.add_company)
        self.add_company_button.grid(row=1, columnspan=2, padx=10, pady=10)

    def add_company(self):
        name = self.company_name_entry.get()
        if name:
            add_company(name)
            messagebox.showinfo("Success", "Firma basariyla eklendi!")
        else:
            messagebox.showerror("Error", "Lutfen bir firma ismi girin.")