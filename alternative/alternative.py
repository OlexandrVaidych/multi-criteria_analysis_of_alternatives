class Alternative:

    def __init__(self, max_convolution, average_convolutions):
        self.max_convolution = max_convolution
        self.average_convolutions = average_convolutions
    
    def select_best_alternative(self):
        for i in self.average_convolutions:
            if self.max_convolution == self.average_convolutions[i]:
                alternative = i
                break        

        return f'The best alternative is {alternative}'