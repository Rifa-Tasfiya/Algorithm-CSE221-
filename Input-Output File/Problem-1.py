""" Problem - 1 File I/O """


# Checking whether the given word is palindrome or NOT
def is_palindrome(word=None):
    if word is None:
        return "not a palindrome"
    else:
        length = len(word)
        i = 0
        while i < (length / 2):
            if word[i] != word[length - 1 - i]:
                return "not a palindrome"
            i += 1
        return "is a palindrome"


# Checking weather the given number is parity or NOT
def is_parity(num):
    if num.isdigit():
        if int(num) % 2 == 0:
            return "has even parity"
        else:
            return "has odd parity"
    else:
        return "cannot have parity"


# Writing the outputs in the output text file
def writing_output_file(num_word):
    global palindrome_check, parity_check
    output_file = open('output.txt', 'a')
    output_file.writelines(
        num_word[0] + " " + parity_check + " and " + num_word[1] + " " + palindrome_check + "\n")

    output_file.close()


# Writing the record file
def write_record_file():
    global line_no, odd_parity_no, even_parity_no, not_parity_no, palindrome_no, non_palindrome_no
    record_file = open("record.txt", "w")
    record_file.write(f"Percentage of odd parity: {int((odd_parity_no / line_no) * 100)} %\n"
                      f"Percentage of even parity: {int((even_parity_no / line_no) * 100)} %\n"
                      f"Percentage of no parity: {int((not_parity_no / line_no) * 100)} %\n"
                      f"Percentage of palindrome: {int((palindrome_no / line_no) * 100)} %\n"
                      f"Percentage of non-palindrome: {int((non_palindrome_no / line_no) * 100)} %")
    record_file.close()


# Opening the input
input_data = open("input.txt")
# Separate the lines and make each line as the element of the line_lst
line_lst = [line.rstrip('\n') for line in input_data]
input_data.close()

# Counting number of lines, odd parity, even parity, not_parity, palindrome, non-palindrome
line_no = 0
odd_parity_no = 0
even_parity_no = 0
not_parity_no = 0
palindrome_no = 0
non_palindrome_no = 0

# Iterating the line list
for i in line_lst:
    num_word_lst = i.split(" ")
    ######## Parity Part
    parity_check = is_parity(num_word_lst[0])
    if parity_check == "has even parity":
        even_parity_no += 1
    elif parity_check == "has odd parity":
        odd_parity_no += 1
    else:
        not_parity_no += 1
    ####### Palindrome Part
    palindrome_check = is_palindrome(num_word_lst[1])
    if palindrome_check == "is a palindrome":
        palindrome_no += 1
    else:
        non_palindrome_no += 1
    # Output file call
    writing_output_file(num_word_lst)
    line_no += 1
# Record file call
write_record_file()
print("Code has been executed!!!!")
