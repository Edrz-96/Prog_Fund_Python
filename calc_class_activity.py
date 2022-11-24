class Calc:

    def __init__(self, num_one, num_two):
        self.num_one = num_one
        self.num_two = num_two

    def __str__(self):
        return f"{self.num_one}({self.num_two})"

    def add(self):
        return self.num_two + self.num_one

    def subtract(self):
        return self.num_two - self.num_one

    def multiply(self):
        return self.num_two * self.num_one

    def divide(self):
        if self.num_two == 0:
            raise Exception("Can't divide by 0!")
        else:
            return self.num_two / self.num_one


new_calc = Calc(1, 2)

