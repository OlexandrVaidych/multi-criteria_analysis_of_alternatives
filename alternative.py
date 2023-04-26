class Alternative:

    def __init__(self, convolutions, average_convolutions):
        self.convolutions = convolutions
        self.average_convolutions = average_convolutions
    
    def select_best_alternative(self):
        max_convolution = max(self.convolutions)
        
        for i in self.average_convolutions:
            if max_convolution == self.average_convolutions[i]:
                alternative = i
                break        

        return f'The best alternative is {alternative}'