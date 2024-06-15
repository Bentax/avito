def spiral_order(matrix):
    if not matrix:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse from top to bottom along the right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left along the bottom row
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top along the left column
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    # Read N
    N = int(data[0])

    # Read matrix
    matrix = []
    for i in range(1, N + 1):
        row = list(map(int, data[i].split()))
        matrix.append(row)

    # Get spiral order
    result = spiral_order(matrix)

    # Print the result as a single line
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()


'''
На вход программы будет подано:Строка из одного числа - N,N строк матрицы.
Каждая строка состоит из N чисел, разделенных пробелом.
Что нужно сделать:Полученную матрицу нужно "развернуть улиткой".
То есть, двигаясь от левого верхнего угла по часовой стрелке, пройтись от краев к центру матрицы и получить все её элементы в виде одной строки.
Sample Input:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Sample Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Напишите программу. Тестируется через stdin → stdout
'''
