class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")
        self.matrix = [item.split() for item in [*self.matrix]]
        
        print(self.matrix)
        
    def row(self, index):
        return [int(item) for item in self.matrix[index-1]]
            

    def column(self, index):
        return [list(int(num) for num in col) for col in zip(*self.matrix)][index-1]