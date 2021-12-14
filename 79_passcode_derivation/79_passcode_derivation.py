class Number:

    def __init__(self, number):
        self.number = number
        self.after = set()
        self.before = set()

    def add_before(self, nbr):
        self.before.add(nbr)

    def add_after(self, nbr):
        self.after.add(nbr)

    def get_before(self):
        return self.before

    def get_after(self):
        return self.after


def get_number(_numbers, _digit):
    for _number in _numbers:
        if _number.number == _digit:
            return _number

with open('../resources/79_passcode_derivation/keylog.txt') as input_file:
    lines = input_file.readlines()
    numbers = []
    out = []
    for line in lines:
        i = 0
        digits = list(line.rstrip())
        for digit in digits:
            number = get_number(numbers, int(digit))
            to_add = False
            if number is None:
                to_add = True
                number = Number(int(digit))
            if i == 0:
                number.add_after(int(digits[1]))
                number.add_after(int(digits[2]))
            if i == 1:
                if number.number == 8 and int(digits[0]) == 8:
                    print('here')
                number.add_before(int(digits[0]))
                number.add_after(int(digits[2]))
            if i == 2:
                if number.number == 8 and (int(digits[0]) == 8 or int(digits[1]) == 8):
                    print('here')
                number.add_before(int(digits[0]))
                number.add_before(int(digits[1]))
            i = i + 1
            if to_add:
                numbers.append(number)

    for number in numbers:
        print(str(number.number) + ' before: ')
        print(*number.get_before())
        print(' after: ')
        print(*number.get_after())
    handled = 0
    after = 0
    while len(numbers) > handled:
        for number in numbers:
            if len(number.get_after()) == after:
                if after == 0:
                    print('Adding: ' + str(number.number))
                    out.append(number.number)
                    handled = handled + 1
                else:
                    for local_after in number.get_after():
                        if local_after not in out:
                            print('For: ' + str(number.number) + ' local after not found: ' + str(local_after))
                    print('Adding: ' + str(number.number))
                    out.insert(0, number.number)
                    handled = handled + 1
        after = after + 1

    print(*out)









