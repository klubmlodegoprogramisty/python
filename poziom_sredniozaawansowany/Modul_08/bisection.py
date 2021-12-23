import matplotlib.pyplot as plt


def func(x):
    return (2 * x ** 3) + (2 * x) - 5


def bisection_task(a: int, b: int, epsilon: float) -> float:
    """obliczamy miejsce zerowe metodą bisekcji"""
    x = (a + b) / 2
    if func(x) == 0:
        return x
    else:
        while abs(a - b) > epsilon:
            x = (a + b) / 2
            if abs(func(x)) < epsilon:
                return x
            else:
                if func(a) * func(x) < 0:
                    b = x
                else:
                    a = x
        else:
            return x


zero_point = bisection_task(-10, 10, 0.000000000000001)
X = [x for x in range(-100, 100)]
Y = [func(x) for x in X]
plt.plot(X, Y, color="blue")
plt.scatter(zero_point, 0, color="red")
plt.grid(True)
plt.title(f"Miejsce zerowe dla f(x)=2x^3+2x-5 = {zero_point}")
plt.show()
