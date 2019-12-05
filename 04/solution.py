from collections import defaultdict

def _decreases(pw):
    """Check that it is decreasing"""
    for i in range(0,5):
        if pw[i] > pw[i+1]:
            return True


def _only_two(pw):
    """Check that only 2 of each number exists"""
    d = defaultdict(int)
    for p in pw:
        d[p] += 1

    return (2 in d.values())


# Part 1
def check(pw, part_1):
    # transform int to list
    pw = [int(p) for p in str(pw)]

    if _decreases(pw):
        return 0

    if part_1:
        for i in range(0,5):
            if pw[i] == pw[i+1]:
                return 1
    else:
        if _only_two(pw):
            return 1

    return 0


def bruteforce():
    # know the range and len() don't bother checking
    counter, counter2 = 0, 0
    for i in range(183564, 657475):
        counter += check(i, True)
        counter2 += check(i, False)

    print('Part 1: ', counter)
    print('Part 2: ', counter2)

if __name__ == '__main__':
   bruteforce()
