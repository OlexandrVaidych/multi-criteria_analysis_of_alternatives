from tkinter import Entry, Label, Tk
from convolution import Convolution
from matrix_column import MatrixColumn
from norm_weight_coeff import NormalizedWeightCoefficient
from criterion import Criterion
from data2 import table_data2
from number import Number
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

    pleasure_point_l = Label(authomated_method_window, text='Pleasure point: ')
    pleasure_point_e = Entry(authomated_method_window)
    pleasure_point_e.insert(0, "20, 20, 15, 20")
   
    num = Number(pleasure_point_e)
    pleasure_point = num.get_nums()
    #print(pleasure_point)

    matrix_column1 = MatrixColumn(criteria1, pleasure_point)
    matrix_elements1 = matrix_column1.calc_matrix_column()
    #print(matrix_elements1)

    convolution1 = Convolution(matrix_elements1, normalized_weight_coefficients1)
    average_convolution1 = convolution1.calc_average_convolution()
    #print(average_convolution1)

    pleasure_point_l.grid(row=5, column=0)
    pleasure_point_e.grid(row=5, column=1)

    authomated_method_window.mainloop()
    