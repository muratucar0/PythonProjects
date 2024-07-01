import tkinter as tk
from tkinter import ttk
import pandas as pd

 
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 23, 32, 35],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

 
root = tk.Tk()
root.title("Pandas ile Veri Görselleştirme")

 
tree = ttk.Treeview(root)

 
tree["columns"] = list(df.columns)
tree.heading("#0", text="Index")
for col in df.columns:
    tree.heading(col, text=col)
 
for i, row in df.iterrows():
    tree.insert("", tk.END, text=i, values=list(row))

 
tree.pack(padx=10, pady=10)

 
root.mainloop()