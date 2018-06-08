
values = {}
values['guitar'] = {}
values['guitar']['weight'] = 1
values['guitar']['value'] = 1500
values['PC'] = {}
values['PC']['weight'] = 3
values['PC']['value'] = 2000
values['audio'] = {}
values['audio']['weight'] = 4
values['audio']['value'] = 3000

total_value = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def find_max_value():
    row = 1
    max_value = 0
    for item in values:
        weight = values[item]['weight']
        value = values[item]['value']
        for j in range(1, len(total_value[row])):
            if weight <= j:
                total_value[row][j] = max(total_value[row-1][j],
                                          value+total_value[row-1][j-weight])
            else:
                total_value[row][j] = total_value[row-1][j]
            if total_value[row][j] > max_value:
                max_value = total_value[row][j]

        row += 1

    return max_value


print(find_max_value())
