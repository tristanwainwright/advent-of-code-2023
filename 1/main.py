from fileinput import input


def is_int(x: any) -> bool:
    try:
        int(x)
        return True
    except:
        return False


def decipher(value: str) -> int:
    numbers = list(filter(is_int, value))
    return int(numbers[0] + numbers[-1])


if __name__ == "__main__":
    sum = 0
    with input('input.txt') as values:
        for value in values:
            sum += decipher(value)
    print(sum)
