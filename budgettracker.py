from tkinter import *
import pandas as pd 
from tkhtmlview import HTMLLabel

class BudgetTracker: 
    def __init__(self, root):
        self.root = root
        self.root.title("Budget App")

root = Tk()
app = BudgetTracker(root)
my_label = HTMLLabel(root, html="""
        <h4>Budget Tracker</h4>
    """)
my_label.pack(pady=20, padx=20)
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
