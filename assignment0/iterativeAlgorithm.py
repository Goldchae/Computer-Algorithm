import time
start = time.time()

def iterative(n):
    a, b = 0, 1
    for _ in range(0, n):
       a, b = b, a + b
    return a

print(iterative(35))
end = time.time()

print(f"{end - start:.5f} sec")