
def load_input():
    lines = []
    with open('input.txt', 'r') as f:
        for line in f:
            for c in line:
                lines.append(int(c))
    return lines


def load_input_as_string():
    with open('input.txt', 'r') as infile:
        for line in infile.readlines():
            return line.strip()


class Solver(object):
    def __init__(self):
        self.width = 25
        self.height = 6
        self.size = self.width * self.height
        self.pixels = load_input()
        self.string_pixels = load_input_as_string()
        self.number_of_layers = len(self.pixels) // self.size
        self.layers = []
        self.buffer = []

    def count(self, layer, value):
        counter = 0
        for d in layer:
            if d == value:
                counter += 1
        return counter

    def load_image(self):
        for i in range(self.number_of_layers):
            self.layers.append(self.pixels[self.size * i: self.size * (i + 1)])

    def painter(self, pixels):
        while len(pixels) > 0:
            for i in range(self.height):
                row = pixels[0:self.width]
                pixels = pixels[self.width:]
                for index, pixel in enumerate(row):
                    if self.buffer[i][index] == '2' and pixel != '2':
                        self.buffer[i][index] = pixel

    def solve_1(self):
        self.load_image()
        min_zeros = float('inf')
        min_zeros_layer = -1

        for i, layer in enumerate(self.layers):
            zeros = self.count(layer, 0)
            if zeros < min_zeros:
                min_zeros = zeros
                min_zeros_layer = i

        print('Part1:', self.count(self.layers[min_zeros_layer], 1) * self.count(self.layers[min_zeros_layer], 2))

    def solve_2(self):
        for _ in range(self.height):
            self.buffer.append(['2'] * self.width)

        self.painter(load_input_as_string())
        for row in self.buffer:
            print(''.join(row).replace('0',' '))


if __name__ == '__main__':
    solver = Solver()
    solver.solve_1()
    solver.solve_2()