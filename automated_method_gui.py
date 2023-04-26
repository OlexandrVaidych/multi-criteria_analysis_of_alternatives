from tkinter import Button, Entry, Label, Tk
from alternative import Alternative
from convolution import Convolution
from matrix_column import MatrixColumn
from norm_weight_coeff import NormalizedWeightCoefficient
from criterion import Criterion
from data2 import table_data2
from number import Number
from table import Table


def authomated_method(window, alternatives, pleasure_point):
    criterion1 = Criterion(table_data2, 1)
    criteria1 = criterion1.get_criteria() 

    criterion2 = Criterion(table_data2, 2)
    criteria2 = criterion2.get_criteria() 

    criterion3 = Criterion(table_data2, 3)
    criteria3 = criterion3.get_criteria() 

    criterion4 = Criterion(table_data2, 4)
    criteria4 = criterion4.get_criteria() 

    normalized_weight_coefficient1 = NormalizedWeightCoefficient(criteria1)
    normalized_weight_coefficients1 = normalized_weight_coefficient1.calc_norm_weight_coeffs()

    normalized_weight_coefficient2 = NormalizedWeightCoefficient(criteria2)
    normalized_weight_coefficients2 = normalized_weight_coefficient2.calc_norm_weight_coeffs()

    normalized_weight_coefficient3 = NormalizedWeightCoefficient(criteria3)
    normalized_weight_coefficients3 = normalized_weight_coefficient3.calc_norm_weight_coeffs()

    normalized_weight_coefficient4 = NormalizedWeightCoefficient(criteria4)
    normalized_weight_coefficients4 = normalized_weight_coefficient4.calc_norm_weight_coeffs()

    matrix_column1 = MatrixColumn(criteria1, pleasure_point)
    matrix_elements1 = matrix_column1.calc_matrix_column()

    matrix_column2 = MatrixColumn(criteria2, pleasure_point)
    matrix_elements2 = matrix_column2.calc_matrix_column()

    matrix_column3 = MatrixColumn(criteria3, pleasure_point)
    matrix_elements3 = matrix_column3.calc_matrix_column()

    matrix_column4 = MatrixColumn(criteria4, pleasure_point)
    matrix_elements4 = matrix_column4.calc_matrix_column()

    convolution1 = Convolution(matrix_elements1, normalized_weight_coefficients1)
    average_convolution1 = convolution1.calc_average_convolution()

    convolution2 = Convolution(matrix_elements2, normalized_weight_coefficients2)
    average_convolution2 = convolution2.calc_average_convolution()

    convolution3 = Convolution(matrix_elements3, normalized_weight_coefficients3)
    average_convolution3 = convolution3.calc_average_convolution()

    convolution4 = Convolution(matrix_elements4, normalized_weight_coefficients4)
    average_convolution4 = convolution4.calc_average_convolution()

    convolutions = [average_convolution1, average_convolution2, average_convolution3, average_convolution4]

    average_convolutions = {
       alternatives[0]: convolutions[0],
       alternatives[1]: convolutions[1],
       alternatives[2]: convolutions[2],
       alternatives[3]: convolutions[3]
       }
    
    alternative = Alternative(convolutions, average_convolutions)
    best_alternative = alternative.select_best_alternative()

    best_alternative_l = Label(window, text=best_alternative)
    best_alternative_l.grid(row=7, column=2)


def authomated_method_gui():
    authomated_method_window = Tk()
    authomated_method_window.geometry("700x265")

    alternatives = ['x1', 'x2', 'x3', 'x4']
    
    table = Table(authomated_method_window, table_data2)
    table.create_table()

    pleasure_point_l = Label(authomated_method_window, text='Pleasure point: ')
    pleasure_point_e = Entry(authomated_method_window)
    pleasure_point_e.insert(0, "20, 20, 15, 20")
   
    num = Number(pleasure_point_e)
    pleasure_point = num.get_nums()

    get_best_alternative_b = Button(
       authomated_method_window, 
       text="The best alternative to determine", 
       command=lambda: authomated_method(authomated_method_window, alternatives, pleasure_point)
       )

    pleasure_point_l.grid(row=5, column=0)
    pleasure_point_e.grid(row=5, column=1)
    get_best_alternative_b.grid(row=6, column=2)

    authomated_method_window.mainloop()
    