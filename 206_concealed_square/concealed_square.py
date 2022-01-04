for i in range(1300000000, 2000000000, 1):
    square = i * i
    string_square = str(square)
    if len(string_square) == 19:
        start = -19
        match = 1
        found_concealed_square = True
        for loop in range(0, 10, 1):
            if start == -1:
                end = None
                match_string = '0'
            else:
                end = start + 1
                match_string = str(match)
            if string_square[start:end] == match_string:
                start = start + 2
                match = match + 1
            else:
                found_concealed_square = False
                break
        if found_concealed_square:
            print('concealed square root: ' +str(i))
            break
