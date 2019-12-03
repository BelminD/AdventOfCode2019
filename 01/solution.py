import math


def get_module_values(doc):
    values = []
    with open(doc) as f:
        for line in f:
            values.append(line)

    return values


def calculate_fuel(mass):
    return math.floor(int(mass) / 3) - 2


# Part 2
def calculate_forgotten_fuel(mass):
    fuel = calculate_fuel(mass)
    answer = fuel
    while fuel > 0:
        fuel = calculate_fuel(fuel)
        if fuel <= 0:
            break
        answer += fuel

    return answer


if __name__ == '__main__':
    values = get_module_values('modules.txt')
    module_fuel = 0
    forgotten_fuel = 0

    for value in values:
        module_fuel += calculate_fuel(value)
    print(module_fuel)

    # Part 2
    for value in values:
        forgotten_fuel += calculate_forgotten_fuel(value)
    print(forgotten_fuel)
