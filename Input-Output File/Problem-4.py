"""Problem 4- Matrix Multiplication: """


# Execute matrix multiplication operation
def multiply_matrix(A, B):
    c = []
    n = len(A)
    for i in range(n):  # Initialize C as a nxn zero matrix
        c.append([0] * n)

    for i in range(0, n):  # Row
        for j in range(0, n):
            for k in range(0, n):
                c[i][j] += int(A[i][k]) * int(B[k][j])
    return c


# Function for reading matrix A and matrix B
def read_matrix(address):
    line_lst = [line.rstrip('\n') for line in address]
    matrix = []
    for i in line_lst:
        i = i.rstrip()
        temp_lst = i.split(" ")
        matrix.append(temp_lst)
    return matrix


def wright_output(product_matrix):
    product_str = "["
    for i in product_matrix:
        product_str = product_str + "\n" + " ["
        for j in i:
            product_str += str(j) + ", "
        product_str = product_str[:-2]
        product_str += "] ,"
    product_str = product_str[:-2]
    product_str = product_str + "\n" + "]"

    # Open and write the output in the output file
    output_file = open("output of AxB.txt", "w")
    output_file.write(product_str)
    output_file.close()


################################## Function calls and open input file##################################################
A_input = open("A matrix input.txt")
A = read_matrix(A_input)
A_input.close()
B_input = open("B matrix input.txt")
B = read_matrix(B_input)
B_input.close()
product_matrix = multiply_matrix(A, B)
wright_output(product_matrix)
print("Code has been executed!!!!")
