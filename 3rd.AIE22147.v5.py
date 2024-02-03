def matrix_multiplication(A, B):
    # Initialize an empty matrix for the result
    result_matrix = []

    # Iterate through each row of matrix A
    for i in range(len(A)):
        row = []

        # Iterate through each column of matrix B
        for j in range(len(B[0])):
            # Calculate the dot product of the current row in A and column in B
            element = sum(A[i][k] * B[k][j] for k in range(len(A[0])))
            row.append(element)

        # Add the row to the result matrix
        result_matrix.append(row)

    return result_matrix

def identity_matrix(size):
    # Create an identity matrix of the given size
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def power_of_matrix(matrix, m):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError('Input matrix should be a square matrix!')
    
    # Initialize the result matrix as the identity matrix
    result_matrix = identity_matrix(len(matrix))
    current_power = m

    # Perform matrix exponentiation using binary exponentiation
    while current_power > 0:
        if current_power % 2 == 1:
            # Multiply the result matrix by the original matrix
            result_matrix = matrix_multiplication(result_matrix, matrix)
        # Square the original matrix for the next iteration
        matrix = matrix_multiplication(matrix, matrix)
        current_power //= 2

    return result_matrix

# this Gets user input for matrix dimension
n = int(input("Matrix Dimension: "))

# it Gets user input for matrix elements
matrix = [[int(input(f"Enter element ({i+1}, {j+1}): ")) for j in range(n)] for i in range(n)]

# Gets user input for the power of the matrix
m = int(input("Enter the power of matrix: "))

# Calculate the result matrix using matrix exponentiation
result_matrix = power_of_matrix(matrix, m)

# Display the result matrix
for row in result_matrix:
    print(row)
