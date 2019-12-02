import pandas as pd

def run():
    data = pd.read_csv('input.txt').astype('int32')
    print('===== PART 1 =====')
    print(sum(x // 3 - 2 for _, x in data.iterrows()))
    print('')

    print('===== PART 2 =====')
    l = data.input.tolist()
    result = 0
    for mass in l:
        s = 0
        fuel = mass // 3 - 2
        while fuel > 0:
            s += fuel
            mass = fuel
            fuel = mass // 3 - 2
        result += s
    print(result)


if __name__=="__main__":
    run()
