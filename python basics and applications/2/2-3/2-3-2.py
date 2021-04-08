def primes():
    i, f = 2, 1
    
    while True:
        if (f + 1) % i == 0:
            yield i
        
        f, i = f * i, i + 1