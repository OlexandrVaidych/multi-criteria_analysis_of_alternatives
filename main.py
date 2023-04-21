from tkinter import Button, Tk
from alternative.alternative_gui import alternative_gui
from automated_method_gui import authomated_method_gui


def main():
    root = Tk()
    root.geometry("250x50")

    alternative_b = Button(
       root, 
       text="The best alternative", 
       command= lambda: alternative_gui()
       )
    
    automated_method_b = Button(
       root, 
       text="Automated method",
       command= lambda: authomated_method_gui()
       )
    
    alternative_b.grid(row=0, column=0)
    automated_method_b.grid(row=0, column=1)
    
    root.mainloop()

if __name__== "__main__":
  main()
