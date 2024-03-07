import time
start = time.time()

def recusive(n):
    if n == 0 or n == 1:
       return n
    else:
       return recusive(n-1) + recusive(n-2)

print(recusive(35))
end = time.time()

print(f"{end - start:.5f} sec")
