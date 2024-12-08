print("Hello, World!")

number_list = list(range(21))
print(number_list)
numbers_up_to_twenty = list(range(21))
print(numbers_up_to_twenty)

number_list = list(range(21))
def squareList(nums):
    squared_list = [num ** 2 for num in nums]
    return squared_list
squared_numbers = squareList(number_list)
print(squared_numbers)

def first_fifteen_elements(nums):
    return nums[:15]
number_list = list(range(21))
squared_numbers = squareList(number_list)
first_fifteen = first_fifteen_elements(squared_numbers)
print(first_fifteen)

def fancy_function(nums):
    reversed_list = nums[::-1]
    return reversed_list[::3]
number_list = list(range(21))
squared_numbers = squareList(number_list)
result = fancy_function(squared_numbers)
print(result)

def create_2d_list():
    matrix = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        matrix.append(row)
    return matrix
matrix = create_2d_list()
print(matrix)     

def modified_2d_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 ==0:
                matrix[i][j] = "?"
    return matrix

def sum_non_question_elements(matrix):
    total_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "?":
                total_sum += matrix[i][j]
    return total_sum
matrix = create_2d_list()
new_matrix = modified_2d_list(matrix)
print(new_matrix)

sum_result = sum_non_question_elements(new_matrix)
print(sum_result)
                    