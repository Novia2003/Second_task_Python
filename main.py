def read_matrix():
    initial_matrix = []

    with open('input.txt', 'r') as file:
        for line in file:
            current_array = []

            for number in line.split(" "):
                current_array.append(int(number))

            initial_matrix.append(current_array)

    print(initial_matrix)

    return initial_matrix


def is_line_sorted(line):
    prev_number = line[0]

    for index in range(1, len(line)):
        if prev_number > line[index]:
            return False
        prev_number = line[index]

    return True


def move_sorted_line_up(matrix):
    index_last_sorted_line_in_up = 0

    for index in range(len(matrix)):
        if is_line_sorted(matrix[index]):
            sorted_line = matrix[index]
            matrix.pop(index)
            matrix.insert(index_last_sorted_line_in_up, sorted_line)
            index_last_sorted_line_in_up += 1


def get_str_from_line(line):
    result_str = ""

    for number in line:
        result_str += str(number) + " "

    result_str += "\n"

    return result_str


def print_result_to_file(matrix):
    print(matrix)
    with open('output.txt', 'w') as file:
        for line in matrix:
            file.write(get_str_from_line(line))


def main():
    matrix = read_matrix()
    move_sorted_line_up(matrix)
    print_result_to_file(matrix)


main()
