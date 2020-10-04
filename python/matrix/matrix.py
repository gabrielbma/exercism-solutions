class Matrix:
    def __init__(self, matrix_string):
        self.matrix = self.__class__._parse_matrix_to_int(matrix_string)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        transposed_matrix = list(map(list, zip(*self.matrix)))
        return transposed_matrix[index - 1]

    @staticmethod
    def _parse_matrix_to_int(matrix_string):
        matrix_chars = [s.split() for s in matrix_string.splitlines()]
        return list(map(lambda x: list(map(int, x)), matrix_chars))
