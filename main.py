from tkinter import Button, Tk
from alternative.alternative_gui import alternative_gui


def main():
    root = Tk()
    root.geometry("100x50")

    alternative_b = Button(
       root, 
       text="The best alternative", 
       command= lambda: alternative_gui()
       )
    
    alternative_b.grid(row=0, column=0)
    root.mainloop()

if __name__== "__main__":
  main()
