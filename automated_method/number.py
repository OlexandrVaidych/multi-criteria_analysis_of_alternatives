class Number:
    
    def __init__(self, pleasure_point_e):
        self.pleasure_point_e = pleasure_point_e
    
    def get_nums(self):
        nums = []
        pleasure_point_str = self.pleasure_point_e.get().split(",")
        
        for i in pleasure_point_str:
            nums.append(int(i))

        return nums