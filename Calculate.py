import math


class Calculate:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_root(self):
        a = self.a
        b = self.b
        c = self.c
        if a == 0:
            return "Not a quadratic equation (a cannot be 0)."
        discriminat = b ** 2 - 4 * a * c
        if discriminat > 0:
            root1 = (-b + math.sqrt(discriminat)) / (2 * a)
            root2 = (-b - math.sqrt(discriminat)) / (2 * a)
            return (root1, root2)
        elif discriminat == 0:
            root = (-b) / (2 * a)
            return (root,)
        else:
            real_part = -b / (2 * a)
            img_part = math.sqrt(-discriminat)
            root1 = complex(real_part, img_part)
            root2 = complex(real_part, -img_part)
            return (root1, root2)

    def show_results(self, result):
        # try:
        #     a = float(input("a: ?"))
        #     b = float(input("b: ?"))
        #     c = float(input("c: ?"))


        if isinstance(result, tuple):
            if len(result) > 1:
                print(f"{result[0]},{result[1]}")
            else:
                print(f"{result[0]}")
        else:
            print(f"{result}")

    @staticmethod
    def get_value():
        try:
            a = float(input("a: ?"))
            b = float(input("b: ?"))
            c = float(input("c: ?"))
            return (a, b, c)
        except ValueError as e:
            print(f" invalid input {e}")
            return None
