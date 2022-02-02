def encode(string):
    encoded_values = []
    count = 1
    def previous(index): return string[index - 1]
    def current(index): return string[index]

    for i in range(1, len(string)):

        if previous(i) != current(i) or count == 9:
            encoded_values.append(str(count) + previous(i))
            count = 0
        count += 1
    encoded_values.append(str(count) + string[len(string)-1])

    return "".join(encoded_values)
