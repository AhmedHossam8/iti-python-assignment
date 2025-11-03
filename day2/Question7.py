import functools
import time

def repeat(n):
    def decorator(func):
        functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

def validate_types(**type_hints):
    def decorator(func):
        def wrapper(*args, **kwargs):
            from inspect import signature
            sig = signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            
            for name, value in bound.arguments.items():
                if name in type_hints:
                    expected_type = type_hints[name]
                    if not isinstance(value, expected_type):
                        raise TypeError(f"Argument '{name}' must be {expected_type.__name__}, "
                                        f"got {type(value).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# @rate_limit(max_calls, time_window)
def rate_limit(max_calls, time_window):
    def decorator(func):
        calls = 0
        start_time = time.time()
        def wrapper(*args, **kwargs):
            nonlocal calls, start_time
            now = time.time()
            
            if now - start_time > time_window:
                start_time = now
                calls = 0
            
            if calls >= max_calls:
                raise Exception("Rate limit reached! Please wait.")
            
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator