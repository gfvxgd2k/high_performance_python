import random
import time

def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
    return False

def search_slow(haystack, needle):
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
    return return_value

def search_unknown1(haystack, needle):
    return any((item == needle for item in haystack))

def search_unknown2(haystack, needle):
    return any([item == needle for item in haystack])

if __name__ == '__main__':
    haystack = random.choices(range(100), k = 100_000)
    needle = 4
    start_time = time.time()
    search_fast(haystack, needle)
    end_time = time.time()
    print(f'search fast: {end_time-start_time}s')

    start_time = time.time()
    search_slow(haystack, needle)
    end_time = time.time()
    print(f'search slow: {end_time-start_time}s')

    start_time = time.time()
    search_unknown1(haystack, needle)
    end_time = time.time()
    print(f'search unknown1: {end_time-start_time}s')

    start_time = time.time()
    search_unknown2(haystack, needle)
    end_time = time.time()
    print(f'search unknown2: {end_time-start_time}s')
