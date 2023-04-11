class Criterion:
        
        def __init__(self, table_data, index):
             self.table_data = table_data
             self.index = index

        def get_criteria(self):
            criteria = []
            for i in range(1, len(self.table_data)):
                for j in range(self.index, self.index + 1):
                    criteria.append(self.table_data[i][j])
            
            return criteria