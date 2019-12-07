from collections import defaultdict


TEST_DATA = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K',  'K)L']


def load_values():
    values = []
    with open('input.txt') as f:
        for line in f:
            values.append(line)

    return values


class Solver(object):

    def __init__(self):
        self.root = 'COM'
        self.values = load_values()
        self.parents = {}
        self.me = 'YOU'
        self.santa = 'SAN'

    # Part 1
    def solve(self):
        for row in self.values:
            a, b = row.strip().split(")")
            self.parents[b] = a

        sum_dist = 0
        for node in self.parents.keys():
            while node != self.root:
                node = self.parents[node]
                sum_dist += 1

        return sum_dist

    # Part 2
    def ancestors(self, node):
        if node == self.root:
            return []
        parent = self.parents[node]
        return self.ancestors(parent) + [parent]

    def solve_2(self):
        a1 = self.ancestors(self.me)
        a2 = self.ancestors(self.santa)

        common = 0
        while a1[common] == a2[common]:
            common += 1

        return len(a1) + len(a2) - 2*common

if __name__ == '__main__':
    solver = Solver()
    print(solver.solve())
    print(solver.solve_2())
