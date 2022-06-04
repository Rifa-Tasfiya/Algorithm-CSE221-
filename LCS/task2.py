# Task-2
def LCS(X, Y):
    zones = {"Y": "Yasnaya", "P": "Pochinki", "S": "School", "R": "Rozhok", "F": "Farm", "M": "Mylta",
             "H": "Shelter", "I": "Prison"}
    m = len(X) + 1
    n = len(Y) + 1
    c = [[0 for i in range(m)] for j in range(n)]  # X=Row & Y= column

    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1

            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]

            else:
                c[i][j] = c[i][j - 1]

    matched = ""
    i = m - 1
    j = n - 1

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            matched += X[i - 1]
            i = i - 1
            j = j - 1
        elif c[i - 1][j] > c[i][j - 1]:
            i = i - 1
        else:
            j = j - 1

    longest_seq = ""
    for i in reversed(matched):
        longest_seq += zones[i] + " "
    # ----------------------------------------- Write Output File-------------------------------------------------------
    output_file = open("task2-output.txt", "w")
    output_file.writelines(f"{longest_seq}\n")
    accuracy_rate = (c[m - 1][n - 1] / no_of_zone) * 100
    output_file.writelines(f"Correctness of prediction: {accuracy_rate}%")
    output_file.close()


input_file = open("task2-input.txt", "r")
no_of_zone = int(input_file.readline())
actual_zone = input_file.readline().strip()
predicted_zone = input_file.readline().strip()
LCS(actual_zone, predicted_zone)
input_file.close()
print("CODE EXECUTED!!!!!!!!!!!!!!!!!!")
