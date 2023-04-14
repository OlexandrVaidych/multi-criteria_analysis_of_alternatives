class Convolution:

    def __init__(self, criteria, norm_weight_coeffs):
        self.criteria = criteria
        self.norm_weight_coeffs = norm_weight_coeffs
    
    def calc_average_convolution(self):
        average_convolution = 0
        for i in range(len(self.criteria)):
            average_convolution += self.criteria[i] * self.norm_weight_coeffs[i]

        return round(average_convolution, 4)

