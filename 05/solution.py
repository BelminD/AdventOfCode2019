import csv


def load_input():
    values = []
    with open('input.csv') as f:
        for row in csv.reader(f):
            for column in row:
                values.append(int(column))

    return values


# I couldn't be bother with creating a Class out of the Solver as I did
# in Day 2, so bare with me, today we are just going to run this badboy
# in a while-loop, it's gonna be great!
def solver(array, input):
    pointer = 0
    output = None

    while True:
        # Pads with 0s infront i.e {1 => 00001}
        inst = str(array[pointer]).zfill(5)
        opcode = int(inst[3:]) # Parses the opcode
        if opcode == 99: # break
            break
        elif opcode == 3: # input
            array[array[pointer+1]] = input
            pointer += 2
        elif opcode == 4: # output
            left = array[pointer+1] if int(inst[2]) else array[array[pointer+1]]
            output = left
            pointer += 2
        elif opcode in [1,2,5,6,7,8]:
            # Broke this out here instead
            left = array[pointer+1] if inst[2] == '1' else array[array[pointer+1]]
            right = array[pointer+2] if inst[1] == '1' else array[array[pointer+2]]
            if opcode == 1: # addition
                array[array[pointer+3]] = left + right
                pointer += 4
            elif opcode == 2: # multiplication
                array[array[pointer+3]] = left * right
                pointer += 4
            elif opcode == 5: # jump-if-true
                if left != 0:
                    pointer = right
                else:
                    pointer += 3
            elif opcode == 6: # jump-if-false
                if left == 0:
                    pointer = right
                else:
                    pointer += 3
            elif opcode == 7: #less-than
                array[array[pointer+3]] = int(left < right)
                pointer += 4
            elif opcode == 8: #equals
                array[array[pointer+3]] = int(left == right)
                pointer += 4
        else:
            # I know I should not raise a generic exception
            # If you see this Pat, I'm sorry
            raise Exception('Invalid Opcode!')

    return output


if __name__ == '__main__':
    print('Part A:', solver(load_input(), 1))
    print('Part B:', solver(load_input(), 5))
