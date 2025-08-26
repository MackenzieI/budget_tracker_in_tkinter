import tkinter as tk
from tkinter import *
import pandas as pd

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class BudgetPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        root.wm_geometry("300x300")

        tk.Label(self, text="Budget Tracker", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, padx=15, pady=15)

        tk.Label(self, text="Date (MM-DD-YYYY): ", font=("Helvetica", 12)).grid(row=1, column=0)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Description: ", font=("Helvetica", 12)).grid(row=2, column=0)
        self.description_entry = tk.Entry(self)
        self.description_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Amount: ", font=("Helvetica", 12)).grid(row=3, column=0)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="Income or Expense: ", font=("Helvetica", 12)).grid(row=4, column=0)
        self.type_entry = tk.Entry(self)
        self.type_entry.grid(row=4, column=1, padx=10, pady=5)

class DebtPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        tk.Label(self, text="Debts", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, padx=15, pady=10)

        tk.Label(self, text="Loan Name: ", font=("Helvetica", 12)).grid(row=1, column=0)

        tk.Label(self, text="Amount: ", font=("Helvetica", 12)).grid(row=2, column=0)

        tk.Label(self, text="Interest Rate (%): ", font=("Helvetica", 12)).grid(row=3, column=0)

# 
# 
# DEBT PAGE IS NOT SHOWN WHEN BUTTON IS CLICKED
#
#

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side="top", fill="x", expand=False)

        self.pages = {}
        for PageClass in (BudgetPage, DebtPage):
            page = PageClass(self.container)
            self.pages[PageClass] = page
            page.place(x=0, y=0, relwidth=1, relheight=1)

        self.debtButton = tk.Button( 
            text="Debt", 
            font=("Helvetica", 12), 
            command=self.pages[BudgetPage].show
        )
        self.debtButton.pack()

        self.pages[BudgetPage].show() 

try: 
    df = pd.read_csv('./records.csv') 
except Exception as e: data = { 
    "Date": [], 
    "Description": [], 
    "Amount": [], 
    "Type": [] 
    } 

df = pd.DataFrame(data)

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
