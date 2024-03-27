import os

def diagonalDifference(matrix):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    matrix_length = len(matrix[0])
    for index in range(matrix_length):
        primary_diagonal_sum += matrix[index][index]
        secondary_diagonal_sum += matrix[index][(matrix_length - index - 1)]
    return abs(primary_diagonal_sum - secondary_diagonal_sum)

def main():
    output_file_path = os.environ['OUTPUT_PATH']
    output_file = open(output_file_path, 'w')

    matrix_size = int(input())
    matrix = []

    for _ in range(matrix_size):
        matrix.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(matrix)

    output_file.write(str(result) + '\n')
    output_file.close()

# Call the main function to execute the program
main()
