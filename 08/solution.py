
def load_input():
    lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            for c in line:
                lines.append(int(c))
    return lines


class Solver(object):
    def __init__(self):
        self.width = 25
        self.height = 6
        self.size = self.width * self.height
        self.pixels = load_input()
        self.number_of_layers = len(self.pixels) // self.size
        self.layers = []

    def count(self, layer, value):
        counter = 0
        for d in layer:
            if d == value:
                counter += 1
        return counter

    def solve_1(self):
        for i in range(self.number_of_layers):
            self.layers.append(self.pixels[self.size * i: self.size * (i + 1)])

        min_zeros = float('inf')
        min_zeros_layer = -1

        for i, layer in enumerate(self.layers):
            zeros = self.count(layer, 0)
            if zeros < min_zeros:
                min_zeros = zeros
                min_zeros_layer = i

        print('Part1:', self.count(self.layers[min_zeros_layer], 1) * self.count(self.layers[min_zeros_layer], 2))


if __name__ == '__main__':
    solver = Solver()
    solver.solve_1()