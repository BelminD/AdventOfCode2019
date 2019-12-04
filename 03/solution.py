import csv


POS = []
DIST = []
STEPS = []


def load_wires():
    wires = []
    with open('input.csv') as f:
        for row in csv.reader(f):
            wires.append(row)
    return wires[0], wires[1]


def build_wire_one(wire, flag):
    x, y = 0, 0
    for w in wire:
        for _ in range(int(w[1:])):
            if w[0] == 'U':
                y += 1
            elif w[0] == 'D':
                y -= 1
            elif w[0] == 'R':
                x += 1
            elif w[0] == 'L':
                x -= 1

            if flag:
                # We just note the first wire and save its values
                POS.append((x, y))
            elif (x, y) in POS:
                # We have already been here i.e we have an intersection
                DIST.append(abs(x) + abs(y))


def build_wire_two(wire, flag):
    x, y = 0, 0
    step = 0
    for w in wire:
        for _ in range(int(w[1:])):
            if w[0] == 'U':
                y += 1
                step += 1
            elif w[0] == 'D':
                y -= 1
                step += 1
            elif w[0] == 'R':
                x += 1
                step += 1
            elif w[0] == 'L':
                x -= 1
                step += 1

            if flag:
                STEPS.append(step)
                POS.append((x, y))
            elif (x, y) in POS:
                DIST.append(STEPS[POS.index((x, y))] + step)


def solution_one(wire0, wire1):
    build_wire_one(wire0, True)
    build_wire_one(wire1, False)
    print(min(DIST))

def solution_two(wire0, wire1):
    build_wire_two(wire0, True)
    build_wire_two(wire1, False)
    print(min(DIST))

if __name__ == '__main__':
    wire0, wire1 = load_wires()
    #solution_one(wire0, wire1)
    #solution_two(wire0, wire1)
