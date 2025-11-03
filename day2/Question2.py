class CustomRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0
        if step == 0:
            raise ValueError("step must not be zero")
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration

        value = self.current
        self.current += self.step
        return round(value, 10)

    def reset(self):
        self.current = self.start

class EvenNumbers(CustomRange):
    def __next__(self):
        while True:
            value = super().__next__()
            if int(value) % 2 == 0:
                return value

def main():
    print("Custom Range 0 to 10:")
    for num in CustomRange(10):
        print(num, end=" ")
        
    print("\n\nCustom Range 5 to 15, step 2:")
    for num in CustomRange(5, 15, 2):
        print(num, end=" ") 
        
    print("\n\nCustom Range 10 to 0, step -2:")
    for num in CustomRange(10, 0, -2):
        print(num, end=" ") 
    
    print("\n\nFloat step - 0 to 2, step 0.5:")
    for num in CustomRange(0, 2, 0.5):
        print(num, end=" ")
    
    print("\n\nEven Numbers 1 to 20:")
    for num in EvenNumbers(1, 20):
        print(num, end=" ")
    
    print("\n\nTest Reset:")
    my_range = CustomRange(3)
    for num in my_range:
        print(num, end=" ")
    print()
    my_range.reset()
    for num in my_range:
        print(num, end=" ")
        
main()