from criterion import Criterion
from table import table_data
from tkinter import Tk
from table import Table

def main():
    root = Tk()
    table = Table(root)
    criterion = Criterion(table_data)
    #print(criterion.get_criteria())

    root.mainloop()



if __name__== "__main__":
  main()
