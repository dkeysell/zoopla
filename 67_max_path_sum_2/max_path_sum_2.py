with open('../resources/67_max_path_sum_2/triangle.txt') as input_file:
    lines = input_file.readlines()
    sums = []
    row_index = 0
    _highest = 0
    for line in lines:
        new_sums = []
        if row_index == 0:
            new_sums.append(int(line))
        else:
            index_in_row = 0
            for value in line.split():
                if index_in_row == 0:
                    _sum = sums[0] + int(value)
                    if _sum > _highest:
                        _highest = _sum
                    new_sums.append(_sum)
                elif len(sums) > index_in_row + 1:
                    _sum1 = sums[index_in_row - 1] + int(value)
                    _sum2 = sums[index_in_row] + int(value)
                    if _sum1 > _sum2:
                        if _sum1 > _highest:
                            _highest = _sum1
                        new_sums.append(_sum1)
                    else:
                        if _sum2 > _highest:
                            _highest = _sum2
                        new_sums.append(_sum2)
                else:
                    _sum = int(value) + sums[index_in_row - 1]
                    if _sum > _highest:
                        _highest = _sum
                    new_sums.append(_sum)
                index_in_row = index_in_row + 1
        row_index = row_index + 1
        sums = new_sums
        print(*sums)


    print(_highest)

