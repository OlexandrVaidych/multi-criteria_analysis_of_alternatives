from convolution import Convolution
from criterion import Criterion
from norm_weight_coeff import NormalizedWeightCoefficient
from table import table_data
from tkinter import Tk
from table import Table

def main():
    root = Tk()
    table = Table(root)

    criterion1 = Criterion(table_data, 1)
    criteria1 = criterion1.get_criteria()
    #print(criteria1)
    
    criterion2 = Criterion(table_data, 2)
    criteria2 = criterion2.get_criteria()
    #print(criteria2)

    criterion3 = Criterion(table_data, 3)
    criteria3 = criterion3.get_criteria()
    print(criteria3)

    criterion4 = Criterion(table_data, 4)
    criteria4 = criterion4.get_criteria()
    print(criteria4)
    
    normalized_weight_coefficient1 = NormalizedWeightCoefficient(criteria1)
    normalized_weight_coefficients1 = normalized_weight_coefficient1.calc_norm_weight_coeffs()
    #print(normalized_weight_coefficients1)

    normalized_weight_coefficient2 = NormalizedWeightCoefficient(criteria2)
    normalized_weight_coefficients2 = normalized_weight_coefficient2.calc_norm_weight_coeffs()
    #print(normalized_weight_coefficients2)

    convolution1 = Convolution(criteria1, normalized_weight_coefficients1)
    average_convolution1 = convolution1.calc_average_convolution()
    #print(average_convolution1)

    convolution2 = Convolution(criteria2, normalized_weight_coefficients2)
    average_convolution2 = convolution2.calc_average_convolution()
    #print(average_convolution2)

    root.mainloop()



if __name__== "__main__":
  main()
