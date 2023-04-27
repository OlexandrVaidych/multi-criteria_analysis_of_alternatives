from tkinter import Button, Label, Tk
from alternatives_analysis.alternatives_analysis import alternatives_analysis_method_gui
from automated_method.automated_method import authomated_method_gui


def main():
    root = Tk()
    root.geometry("450x100")

    title_l = Label(
       root, 
       text="Determining the best alternative using multicriteria methods", 
       font=('Times', 14)
       )

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
    
    title_l.pack()
    alternatives_analysis_method_b.pack(side='left', padx=30)
    automated_method_b.pack(side='right', padx=30)
    
    root.mainloop()

if __name__== "__main__":
  main()
