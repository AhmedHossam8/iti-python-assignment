def infinite_counter(start=0, step=1):
    n = start
    while True:
        yield n
        n += step
        
def cycle_list(items):
    while True:
        for item in items:
            yield item

def fibonacci_infinite():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        
def prime_generator_infinite():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def alternating(*generators):
    gens = list(generators)
    i = 0
    while True:
        if not gens:
            return
        value = next(gens[i])
        yield value
        i = (i + 1) % len(gens)

def take(n, generator):
    count = 0
    for item in generator:
        if count >= n:
            break
        yield item
        count += 1

def skip(n, generator):
    for i in range(n):
        next(generator, None)
    for item in generator:
        yield item


print("First 10 numbers from counter:")
counter = infinite_counter(1, 2)
for num in take(10, counter):
    print(num, end=" ")

print("\n\nCycle through list:")
colors = cycle_list(['red', 'green', 'blue'])
for color in take(7, colors):
    print(color, end=" ")

print("\n\nFirst 15 Fibonacci numbers:")
fib = fibonacci_infinite()
for num in take(15, fib):
    print(num, end=" ")

print("\n\nFirst 10 prime numbers:")
primes = prime_generator_infinite()
for p in take(10, primes):
    print(p, end=" ")

print("\n\nAlternating generators:")
gen1 = infinite_counter(1)
gen2 = infinite_counter(100, 100)
alt = alternating(gen1, gen2)
for num in take(8, alt):
    print(num, end=" ")

print("\n\nSkip first 5 from counter:")
counter = infinite_counter()
skipped = skip(5, counter)
for num in take(5, skipped):
    print(num, end=" ")

# Using generator with condition
print("\n\nFirst 10 even Fibonacci numbers:")
fib = fibonacci_infinite()
even_fib = (x for x in fib if x % 2 == 0)
for num in take(10, even_fib):
    print(num, end=" ")