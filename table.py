from tkinter import END, Entry


class Table:
    def __init__(self, window, table_data):
        self.window = window
        self.table_data = table_data
    
    def create_table(self):
        rows_total = len(self.table_data)
        columns_total = len(self.table_data[0])

        for i in range(rows_total):
            for j in range(columns_total):
                e = Entry(self.window)
                e.grid(row=i, column=j)
                e.insert(END, self.table_data[i][j])
