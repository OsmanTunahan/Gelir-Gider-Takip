from app.gui.main_window import IncomeExpenseTrackerApp
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    app = IncomeExpenseTrackerApp(root)
    root.mainloop()