import pandas as pd
import itertools

def run():
    with open('input.txt', 'r') as file:
        data = file.read().split(',')
    data = [int(x) for x in data]

    print('=== Part 1 ===')
    program_1202 = list(data)
    program_1202[1] = 12
    program_1202[2] = 2
    print(start(program_1202)[0])
    print()
    print('=== Part 2 ===')
    for a, b in itertools.product(range(0,100), range(0,100)):
        program_data = list(data)
        program_data[1] = a
        program_data[2] = b
        output = start(program_data)[0]
        if output == 19690720:
            print(100*a + b)



def start(data):
    index = 0
    while index < len(data):
        opcode = data[index]
        if opcode == 1 or opcode == 2:
            op_1 = data[index + 1]
            op_2 = data[index + 2]
            op_3 = data[index + 3]
            v_1 = data[op_1]
            v_2 = data[op_2]
            data[op_3] = v_1 + v_2 if opcode == 1 else v_1 * v_2
            index += 4
        elif opcode == 99:
            break
        else:
            print('ERROR')
            break
    if opcode != 99:
        print('NOT FINISHED WITH 99')
    return data

if __name__ == '__main__':
    run()
