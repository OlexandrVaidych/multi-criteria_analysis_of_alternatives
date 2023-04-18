from alternative import Alternative
from convolution import Convolution
from criterion import Criterion
from norm_weight_coeff import NormalizedWeightCoefficient
from table import table_data
from tkinter import Tk
from table import Table

def main():
    root = Tk()
    table = Table(root)
    alternatives = ['x1', 'x2', 'x3', 'x4']

    criterion1 = Criterion(table_data, 1)
    criteria1 = criterion1.get_criteria()
    #print(criteria1)
    
    criterion2 = Criterion(table_data, 2)
    criteria2 = criterion2.get_criteria()
    #print(criteria2)

    criterion3 = Criterion(table_data, 3)
    criteria3 = criterion3.get_criteria()
    #print(criteria3)

    criterion4 = Criterion(table_data, 4)
    criteria4 = criterion4.get_criteria()
    #print(criteria4)
    
    normalized_weight_coefficient1 = NormalizedWeightCoefficient(criteria1)
    normalized_weight_coefficients1 = normalized_weight_coefficient1.calc_norm_weight_coeffs()
    #print(normalized_weight_coefficients1)

    normalized_weight_coefficient2 = NormalizedWeightCoefficient(criteria2)
    normalized_weight_coefficients2 = normalized_weight_coefficient2.calc_norm_weight_coeffs()
    #print(normalized_weight_coefficients2)

    normalized_weight_coefficient3 = NormalizedWeightCoefficient(criteria3)
    normalized_weight_coefficients3 = normalized_weight_coefficient3.calc_norm_weight_coeffs()
    #print(normalized_weight_coefficients3)

    normalized_weight_coefficient4 = NormalizedWeightCoefficient(criteria4)
    normalized_weight_coefficients4 = normalized_weight_coefficient4.calc_norm_weight_coeffs()
    #print(normalized_weight_coefficients4)

    convolution1 = Convolution(criteria1, normalized_weight_coefficients1)
    average_convolution1 = convolution1.calc_average_convolution()
    #print(average_convolution1)

    convolution2 = Convolution(criteria2, normalized_weight_coefficients2)
    average_convolution2 = convolution2.calc_average_convolution()
    #print(average_convolution2)

    convolution3 = Convolution(criteria3, normalized_weight_coefficients3)
    average_convolution3 = convolution3.calc_average_convolution()
    #print(average_convolution3)

    convolution4 = Convolution(criteria4, normalized_weight_coefficients4)
    average_convolution4 = convolution4.calc_average_convolution()
    #print(average_convolution4)

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
    #print(best_alternative)

    root.mainloop()


if __name__== "__main__":
  main()
