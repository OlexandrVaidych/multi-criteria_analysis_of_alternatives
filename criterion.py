class Criterion:
        
        def __init__(self, table_data):
             self.table_data = table_data

        def get_criteria(self):
            criteria = []
            for i in range(1, len(self.table_data)):
                for j in range(1, len(self.table_data[1])):
                    criteria.append(self.table_data[i][j])
            
            return criteria