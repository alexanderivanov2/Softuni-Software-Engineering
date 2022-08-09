class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            result = self.func(*args, **kwargs)
            txt = f"Function {self.func.__name__} was add called. Result: {result}"
            file.write(txt + "\n")
            return txt


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
