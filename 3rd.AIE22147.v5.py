def matrix_multiplication(A, B):
    #we create an empty matrix for calculating the result(array)
    result_matrix = []
#we go through each row of A matrix by keeping the row constant
    for i in range(len(A)):
        row = []
#we go through each column of B matrix of the row(A matrix)
        for j in range(len(B[0])):
   #we do dot product for the current roww of A and column in B
            element = sum(A[i][k] * B[k][j] for k in range(len(A[0])))
            row.append(element)
#adding the row to the resulkt matrix
        result_matrix.append(row)

    return result_matrix

def identity_matrix(size):
    # Creating an identity matrix.
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def power_of_matrix(matrix, m):
    # Check if the matrix is square(as per the given condition)
    if len(matrix) != len(matrix[0]):
        raise ValueError('Input matrix should be a square matrix!')
    
    # we keep the result matrix as the identity matrix
    result_matrix = identity_matrix(len(matrix))
    current_power = m

    # Performing matrix exponentiation using binary exponentiation (for finding the power)
    while current_power > 0:
        if current_power % 2 == 1:
            result_matrix = matrix_multiplication(result_matrix, matrix)
            #(it is responsible for updating the result matrix (result_matrix) during each iteration of the loop)
        # Square the original matrix for the next iteration
        matrix = matrix_multiplication(matrix, matrix)
        current_power //= 2

    return result_matrix
n = int(input("Matrix Dimension: "))
#taking the input of the matrix the user wants to enter
matrix = [[int(input(f"Enter element ({i+1}, {j+1}): ")) for j in range(n)] for i in range(n)]

#user inputs the power of the matrix...
m = int(input("Enter the power of matrix: "))

# call the function for calculating the power of the matrix and stores in the result matrix
result_matrix = power_of_matrix(matrix, m)

# Displays  result matrix
for row in result_matrix:
    print(row)
