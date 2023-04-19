from tkinter import Button, Label, Tk
from alternative.alternative import Alternative
from alternative.convolution import Convolution
from alternative.criterion import Criterion
from alternative.data import table_data
from alternative.norm_weight_coeff import NormalizedWeightCoefficient
from alternative.table import Table


def get_best_alternative(alternative_window):
    alternatives = ['x1', 'x2', 'x3', 'x4']

    criterion1 = Criterion(table_data, 1)
    criteria1 = criterion1.get_criteria()
    
    criterion2 = Criterion(table_data, 2)
    criteria2 = criterion2.get_criteria()

    criterion3 = Criterion(table_data, 3)
    criteria3 = criterion3.get_criteria()

    criterion4 = Criterion(table_data, 4)
    criteria4 = criterion4.get_criteria()
    
    normalized_weight_coefficient1 = NormalizedWeightCoefficient(criteria1)
    normalized_weight_coefficients1 = normalized_weight_coefficient1.calc_norm_weight_coeffs()

    normalized_weight_coefficient2 = NormalizedWeightCoefficient(criteria2)
    normalized_weight_coefficients2 = normalized_weight_coefficient2.calc_norm_weight_coeffs()

    normalized_weight_coefficient3 = NormalizedWeightCoefficient(criteria3)
    normalized_weight_coefficients3 = normalized_weight_coefficient3.calc_norm_weight_coeffs()

    normalized_weight_coefficient4 = NormalizedWeightCoefficient(criteria4)
    normalized_weight_coefficients4 = normalized_weight_coefficient4.calc_norm_weight_coeffs()

    convolution1 = Convolution(criteria1, normalized_weight_coefficients1)
    average_convolution1 = convolution1.calc_average_convolution()

    convolution2 = Convolution(criteria2, normalized_weight_coefficients2)
    average_convolution2 = convolution2.calc_average_convolution()

    convolution3 = Convolution(criteria3, normalized_weight_coefficients3)
    average_convolution3 = convolution3.calc_average_convolution()

    convolution4 = Convolution(criteria4, normalized_weight_coefficients4)
    average_convolution4 = convolution4.calc_average_convolution()

    convolutions = [average_convolution1, average_convolution2, average_convolution3, average_convolution4]
    average_convolutions = {
       alternatives[0]: convolutions[0],
       alternatives[1]: convolutions[1],
       alternatives[2]: convolutions[2],
       alternatives[3]: convolutions[3]
       }
    
    max_convolution = max(convolutions)

    alternative = Alternative(max_convolution, average_convolutions)
    best_alternative = alternative.select_best_alternative()

    best_alternative_l = Label(alternative_window, text=best_alternative)
    best_alternative_l.grid(row=12, column=2)

def alternative_gui():
    alternative_window = Tk()
    alternative_window.geometry("700x265")
    table = Table(alternative_window)
    empty_l = Label(alternative_window)
    
    get_best_alternative_b = Button(
       alternative_window, 
       text="The best alternative to determine", 
       command=lambda: get_best_alternative(alternative_window)
       )
    
    empty_l.grid(row=10, column=2)
    get_best_alternative_b.grid(row=11, column=2)
    
    alternative_window.mainloop()
