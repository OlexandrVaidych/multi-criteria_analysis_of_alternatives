from tkinter import END, Entry
from data import table_data

class Table:

    def __init__(self, root):
        
        for i in range(rows_total):
            for j in range(columns_total):

                self.e = Entry(root)
                self.e.grid(row=i, column=j)
                self.e.insert(END, table_data[i][j])

rows_total = len(table_data)
columns_total = len(table_data[0])