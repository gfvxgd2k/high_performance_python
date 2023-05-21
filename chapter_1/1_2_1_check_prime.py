import math

def check_prime(number):
    sqrt_number = math.sqrt(number)
    for i in range(2,int(sqrt_number) + 1):
        if (number / i).is_integer():
            return False
    return True

def check_prime_better(number):
    #FIXME must be fixed after chapter 6
    sqrt_number = math.sqrt(number)
    numbers = range(2, int(sqrt_number) + 1)
    for i in range(0, len(numbers), 5):
        result = (number / numbers[i:(i + 5)]).is_integer()
        if any(result):
            return False
    return True

if __name__ == '__main__':
    print(f'check_prime(10,000,000) = {check_prime(10_000_000)}')
    print(f'check_prime(10,000,019) = {check_prime(10_000_019)}')