import time

start = time.time()

result1 = sum(range(1, 1000001))
result2 = 2 * 1000000

end = time.time()

time = end - start
print(f"Execution time: {time:.5f} seconds")