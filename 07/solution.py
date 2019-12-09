import csv
import itertools

from intcode import Intcode


def load_input():
    values = []
    with open('input.csv') as f:
        for row in csv.reader(f):
            for column in row:
                values.append(int(column))

    return values


class Circuit(object):
    def __init__(self, phase):
        self.m0 = Intcode(int(phase[0]))
        self.m1 = Intcode(int(phase[1]))
        self.m2 = Intcode(int(phase[2]))
        self.m3 = Intcode(int(phase[3]))
        self.m4 = Intcode(int(phase[4]))

    def run(self, inp):
        array = load_input()
        # array = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        value = self.m0.run(array, inp)
        value = self.m1.run(array, value)
        value = self.m2.run(array, value)
        value = self.m3.run(array, value)
        return self.m4.run(array, value)


def solve_1():
    outputs = []
    perms = list(itertools.permutations(range(5)))
    for perm in perms:
        circuit = Circuit(perm)
        outputs.append(circuit.run(0))

    max_value = max(outputs)
    ind = outputs.index(max_value)
    print('Part 1: {}, {}'.format(max_value, perms[ind]))

# Not working
def solve_2():
    outputs = []
    perms = list(itertools.permutations([5,6,7,8,9]))
    for perm in perms:
        circuit = Circuit(perm)
        output = circuit.run(0)
        output = circuit.run(output)
        outputs.append(output)
    max_value = max(outputs)
    ind = outputs.index(max_value)
    print('Part 2: {}, {}'.format(max_value, perms[ind]))

if __name__ == '__main__':
    # solve_1()
    solve_2()