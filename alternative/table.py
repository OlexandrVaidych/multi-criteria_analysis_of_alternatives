from tkinter import END, Entry
from alternative.data import table_data

class Table:

    def __init__(self, alternative_window):
        
        for i in range(rows_total):
            for j in range(columns_total):

                self.e = Entry(alternative_window)
                self.e.grid(row=i, column=j)
                self.e.insert(END, table_data[i][j])

rows_total = len(table_data)
columns_total = len(table_data[0])