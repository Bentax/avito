def rotate_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    rotated = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            rotated[j][n-1-i] = matrix[i][j]
    
    return rotated

def main():
    import sys
    input = sys.stdin.read
    
    # Reading input from stdin
    lines = input().strip().split('\n')
    
    # Constructing the matrix from input
    matrix = []
    for line in lines:
        row = list(map(int, line.split()))
        matrix.append(row)
    
    # Rotating the matrix 90 degrees clockwise
    rotated_matrix = rotate_matrix(matrix)
    
    # Printing the rotated matrix to stdout
    for row in rotated_matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()

'''
Дана квадратная матрица размера n из чисел из интервала [1, 100]. Размер матрицы может быть произвольным, в интервале [1, 10].
Напишите программу на Python без использования внешних библиотек, которая:

Считает матрицу из stdin
Повернет матрицу на 90 градусов по часовой стрелке.
Формат данных на входе:
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
На вход подаются элементы матрицы построчно. Нужно определить размер матрицы исходя из входных данных, после чего провести преобразования и вывести преобразованную матрицу в консоль.

Формат данных на выходе:

21 16 11 6 1
22 17 12 7 2
23 18 13 8 3
24 19 14 9 4
25 20 15 10 5
'''
