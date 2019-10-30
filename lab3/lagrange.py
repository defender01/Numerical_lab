import numpy as np
import matplotlib.pyplot as plt


def lagrange_InterPolation(X, x, Y, n):
    result = 0.0
    for i in range(n):
        s = 1.0
        t = 1.0

        for j in range(n):

            if (i != j):
                s = s * (x - X[j])
                t = t * (X[i] - X[j])

        result = result + (s / t) * Y[i]
    return result


X = np.array([-7., -9., 0., 9., 8., 3., -3.])
print(X)
Y = np.array([2., 8., 1., 9., 5., -3., -7.])
print(Y)

ans = lagrange_InterPolation(X, 2, Y, 3)
print(ans)

xp = np.linspace(-10, 10, 100)
# print(xp)
yp = lagrange_InterPolation(X, xp, Y, 7)
plt.plot(xp, yp, '-', X, Y, 'ro')


plt.show()