def run():
    minimum = 382345
    maximum = 843167
    numbers = []
    for number in range(minimum, maximum + 1):
        if not has_adjacent_digits(number):
            continue

        if not is_increasing(number):
            continue
        
        numbers.append(number)
    print('=== Part 1 ===')
    print(len(numbers))

def is_increasing(number: int):
    current_digit = number % 10
    lowest_digit = current_digit
    rest = number // 10
    while rest > 0:
        current_digit = rest % 10
        if current_digit > lowest_digit:
            return False
        lowest_digit = current_digit
        rest //= 10
        
    return True

def has_adjacent_digits(number: int):
    digit_1 = number % 10
    rest = number // 10
    while rest > 0:
        digit_2 = rest % 10
        if digit_1 == digit_2:
            return True
        rest //= 10
        digit_1 = digit_2
        
    return False

if __name__ == "__main__":
    run()
