from tkinter import Tk
from norm_weight_coeff import NormalizedWeightCoefficient
from criterion import Criterion
from data2 import table_data2
from table import Table


def authomated_method_gui():
    authomated_method_window = Tk()
    authomated_method_window.geometry("700x265")
    
    table = Table(authomated_method_window, table_data2)
    table.create_table()

    criterion1 = Criterion(table_data2, 1)
    criteria1 = criterion1.get_criteria() 
    #print(criteria1)

    normalized_weight_coefficient1 = NormalizedWeightCoefficient(criteria1)
    normalized_weight_coefficients1 = normalized_weight_coefficient1.calc_norm_weight_coeffs()
    #print(normalized_weight_coefficients1)

    """
    empty_l = Label(alternative_window)
    
    get_best_alternative_b = Button(
       alternative_window, 
       text="The best alternative to determine", 
       command=lambda: get_best_alternative(alternative_window)
       )
    
    empty_l.grid(row=10, column=2)
    get_best_alternative_b.grid(row=11, column=2)
    """

    authomated_method_window.mainloop()
    