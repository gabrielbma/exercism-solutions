class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [
            [int(col) for col in line.split()] for line in matrix_string.splitlines()
        ]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        transposed_matrix = list(map(list, zip(*self.matrix)))
        return transposed_matrix[index - 1]
