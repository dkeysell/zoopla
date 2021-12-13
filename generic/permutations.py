def solution(input: int) -> int:
    input_array = list(str(input))
    return calc_permutations(input_array, '', [])


def calc_permutations(input_array, out_string, permutations):
    for i in range(0, len(input_array)):
        if len(input_array) == 1:
            out_string = out_string + input_array[0]
            permutations.append(out_string)
        else:
            popped = input_array.pop(i)
            out_string = out_string + popped
            calc_permutations(input_array, out_string, permutations)
            out_string = out_string[:-1]
            input_array.insert(i, popped)
    return permutations

