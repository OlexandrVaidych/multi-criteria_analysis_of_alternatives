class Convolution:

    def __init__(self, elements, norm_weight_coeffs):
        self.elements = elements
        self.norm_weight_coeffs = norm_weight_coeffs
    
    def calc_average_convolution(self):
        average_convolution = 0
        for i in range(len(self.elements)):
            average_convolution += self.elements[i] * self.norm_weight_coeffs[i]

        return round(average_convolution, 4)

