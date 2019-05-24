def matrix_divided(matrix, div):
    """ Divides all elements of matrix"""
    result = 0
    nuevo = []
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not div:
        raise TypeError("div must be a number")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if matrix:
        for row in matrix:
            temp = []
            lenirow = matrix[0]
            if len(row) == 0:
                raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")
            if len(lenirow) != len(row):
                raise TypeError("Each row of the matrix must have the same s\
                        ize")
            for j in row:
                if type(j) != int and type(j) != float:
                    raise TypeError("matrix must be a matrix (list of lists) o\
                            f integers/floats")
                result = j / div
                result = round(result, 2)
                temp.append(result)
            nuevo.append(temp)
        return nuevo
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers\
                /floats")
