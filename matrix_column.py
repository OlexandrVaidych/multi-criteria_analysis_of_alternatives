class MatrixColumn():

    def __init__(self, criteria, pleasure_point):
        self.criteria = criteria
        self.pleasure_point = pleasure_point
    
    def calc_matrix_column(self):
        matrix_column = []

        criteria_len = len(self.criteria)
        criteria_min = min(self.criteria)
        criteria_max = max(self.criteria)

        for i in range(criteria_len):
            matrix_el = 1 - (abs(self.pleasure_point[i] - self.criteria[i])) / max(self.pleasure_point[i] - criteria_min, 
                                                                                   criteria_max - self.pleasure_point[i])
            matrix_column.append(round(matrix_el, 2))
    
        return matrix_column
    
    

