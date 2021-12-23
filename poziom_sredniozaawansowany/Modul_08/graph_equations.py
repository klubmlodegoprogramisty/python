def graph_system_equation() -> None:
    import matplotlib.pyplot as plt

    def indicators(a1: int, b1: int, c1: int, a2: int, b2: int, c2: int) -> tuple:
        """obliczamy układ równań metodą wyznaczników"""
        w = a1 * b2 - b1 * a2
        wx = c1 * b2 - b1 * c2
        wy = a1 * c2 - c1 * a2

        if w:
            return (wx / w, wy / w)
        else:
            return None

    def f1(x: int) -> float:
        return 1.25 * x - 2

    def f2(x: int) -> float:
        return -2 * x + 11

    result_point = indicators(5, -4, 8, 4, 2, 22)
    if result_point:
        W0 = [result_point[0]]
        W1 = [result_point[1]]
        plt.scatter(W0, W1, color="red")

    X0 = [x for x in range(-10, 20)]
    Y1 = [f1(x) for x in range(-10, 20)]
    Y2 = [f2(x) for x in range(-10, 20)]

    plt.plot(X0, Y1)
    plt.plot(X0, Y2)
    plt.grid(True)
    plt.title(f"Wynik rozwiązania układu równań to punkt {result_point}")
    plt.legend(["Punkt","Wynik funkcji f(x)=1.25*x-2", "Wynik funkcji f(x)=-2*x+11"])
    plt.show()

graph_system_equation()
