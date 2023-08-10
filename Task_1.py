#Напишите функцию для транспонирования матрицы Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transpon(matrix):
    width = len(matrix[0])
    height = len(matrix)
    res = [[0]*height for i in range(width)]
    i = 0

    while (i < width):
        j = 0
        while (j < height):
            res[i][j] = matrix[j][i]
            j += 1
        i += 1

    return res
   
print(transpon([[1, 2, 3], [4, 5, 6]])) # [[1, 4], [2, 5], [3, 6]]