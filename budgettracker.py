import tkinter as tk
from tkinter import *
import pandas as pd 

class BudgetTracker: 
    def __init__(self, root):
        self.root = root
        self.root.title("Budget App")

        self.my_label = tk.Label(root, text="Budget Tracker", font=("Helvetica", 14, "bold"), justify=tk.CENTER)
        self.my_label.grid(row=0,column=0, columnspan=2, padx=15,pady=15)

        self.date_label = tk.Label(root, text="Date (MM-DD-YYYY): ", font=("Helvetica", 12), justify=tk.LEFT)
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        self.description_label = tk.Label(root, text="Description: ", font=("Helvetica", 12))
        self.description_label.grid(row=2,column=0)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=2,column=1, padx=10, pady=5)        
        
        self.amount_label = tk.Label(root, text="Amount: ", font=("Helvetica", 12))
        self.amount_label.grid(row=3,column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=3,column=1, padx=10, pady=10)        
        
        self.type_label = tk.Label(root, text="Income or expense: ", font=("Helvetica", 12))
        self.type_label.grid(row=4,column=0)
        self.type_entry = tk.Entry(root)
        self.type_entry.grid(row=4,column=1, padx=10, pady=10)

root = Tk()
app = BudgetTracker(root)
root.mainloop()

try:
    df = pd.read_csv('./records.csv')
except Exception as e: 
    data = {
        "Date": [],
        "Description": [],
        "Amount": [],
        "Type": []
    }
    
    df = pd.DataFrame(data)
