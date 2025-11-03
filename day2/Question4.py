import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[TIMER] Function '{func.__name__}' executed in {end - start:.4f} seconds")
        return result
    return wrapper

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOGGER] Calling function '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOGGER] Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__} with:")
        print(f"  Positional args: {args}")
        print(f"  Keyword args: {kwargs}")
        
        result = func(*args, **kwargs)

        print(f"[DEBUG] {func.__name__} returned {result!r}")
        return result
    return wrapper


# Run
@timer
def slow_function(n):
    time.sleep(n)
    return f"Slept for {n} seconds"
print(slow_function(2))

@logger
def add(a, b):
    return a + b

add(5, 3)

@count_calls
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
greet("Bob")
greet("Charlie")
print(f"Total calls: {greet.call_count}")

@debug
def multiply(x, y):
    return x * y

multiply(4, 7)