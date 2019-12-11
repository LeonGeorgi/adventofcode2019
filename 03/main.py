import numpy as np

def run():
    with open('input.txt', 'r') as file:
        data = file.read().split('\n')
    cable_1 = data[0].split(',')
    cable_2 = data[1].split(',')


    print('=== Part 1 ===')
    d = {}
    costs = 0
    x, y = 0, 0
    for command in cable_1:
        direction = command[0]
        count = int(command[1:])
        for _ in range(count):
            if direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1
            costs += 1
            if (x, y) not in d:
                d[(x, y)] = costs
    e = {}
    costs = 0
    x, y = 0, 0
    for command in cable_2:
        direction = command[0]
        count = int(command[1:])
        for _ in range(count):
            if direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1
            costs += 1
            if (x, y) in d and (x, y) not in e:
                e[(x, y)] = d[(x, y)] + costs

    m = min(e, key=lambda t: abs(t[0]) + abs(t[1]))
    print(abs(m[0]) + abs(m[1]))
    print()


    print('=== Part 2 ===')
    m = min(e.items(), key=lambda item: item[1])
    print(m[1])



def start(data):
    pass

if __name__ == '__main__':
    run()
