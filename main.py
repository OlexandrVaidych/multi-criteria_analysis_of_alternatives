from tkinter import Button, Tk
from alternatives_analysis import alternatives_analysis_method_gui
from automated_method.automated_method import authomated_method_gui


def main():
    root = Tk()
    root.geometry("300x50")

    alternatives_analysis_method_b = Button(
       root, 
       text="Alternatives analysis method", 
       command= lambda: alternatives_analysis_method_gui()
       )
    
    automated_method_b = Button(
       root, 
       text="Automated method",
       command= lambda: authomated_method_gui()
       )
    
    alternatives_analysis_method_b.grid(row=0, column=0)
    automated_method_b.grid(row=0, column=1)
    
    root.mainloop()

if __name__== "__main__":
  main()
