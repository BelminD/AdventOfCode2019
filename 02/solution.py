import csv
import sys


def _get_values():
    values = []
    with open('ints.csv') as f:
        for row in csv.reader(f):
            for column in row:
                values.append(int(column))

    return values


class Solver(object):
    def __init__(self, array):
        self.array = array
        self.pointer = 0

    def switcher(self):
        method_name = 'opcode_' + str(self.array[self.pointer])
        method = getattr(self, method_name, lambda: 'Invalid opcode')
        return method()

    def opcode_1(self):
        self.array[self.array[self.pointer + 3]] = (
            self.array[self.array[self.pointer + 1]]
            + self.array[self.array[self.pointer + 2]]
        )
        self.pointer += 4

    def opcode_2(self):
        self.array[self.array[self.pointer + 3]] = (
            self.array[self.array[self.pointer + 1]]
            * self.array[self.array[self.pointer + 2]]
        )
        self.pointer += 4

    def opcode_99(self):
        print('Halt!', self.array[0])
        sys.exit(0)


class BruteSolver(Solver):
    def __init__(self, array):
        super().__init__(array)
        self.answer = 19690720

    def opcode_99(self):
        if self.array[0] == self.answer:
            print('Noun = ', self.array[1])
            print('Verb = ', self.array[2])
            print('Answer =', 100 * self.array[1] + self.array[2])
            sys.exit(0)
        return True


def bruteforce():
    brutesolver = BruteSolver(_get_values())
    for i in range(0, 100):
        brutesolver.array[1] = i
        for j in range(0, 100):
            brutesolver.array[2] = j
            while True:
                if brutesolver.switcher():
                    break

            # Reset values
            brutesolver.array = _get_values()
            brutesolver.array[1] = i
            brutesolver.pointer = 0

        # Reset value
        brutesolver.array = _get_values()


if __name__ == '__main__':
    # Part 1
    # solver = Solver(array=_get_values())
    # while True:
        # solver.switcher()

    # Part 2
    bruteforce()
