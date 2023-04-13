class NormalizedWeightCoefficient:
    
    def __init__(self, criteria):
        self.criteria = criteria
    
    def calc_norm_weight_coeffs(self):
        norm_weight_coeffs = []
        criteria_len = len(self.criteria)

        for i in range(0, criteria_len):
            criteria_sum = 0
            for j in range(i, criteria_len):
                criteria_sum += self.criteria[j]
        
            norm_weight_coeff = self.criteria[i] / criteria_sum

            norm_weight_coeffs.append(round(norm_weight_coeff, 2))
        
        return norm_weight_coeffs
