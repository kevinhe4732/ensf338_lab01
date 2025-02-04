import time

def pow2(n):
    """
    Generates the n-th power of 2 (i.e., 2^n).
    """
    return 2 ** n

def pow2_loop(n):
    """
    Generates the n-th power of 2 (i.e., 2^n) using a loop.
    """
    result = 1
    for _ in range(n):
        result *= 2
    return result

def pow2_list(n):
    """
    Generates the n-th power of 2 (i.e., 2^n) using list comprehension.
    """
    return [2 ** i for i in range(n)]

if __name__ == "__main__":
    # Test pow2(10000)
    start_time = time.time()
    pow2(10000)
    print(f"Time for pow2(10000): {time.time() - start_time:.5f} seconds")

    # Test pow2_loop(1000) and pow2_list(1000)
    for func in [pow2_loop, pow2_list]:
        total_time = 0
        for _ in range(1000):
            start_time = time.time()
            func(1000)
            total_time += time.time() - start_time
        print(f"Average time for {func.__name__}(1000): {total_time / 1000:.5f} seconds")