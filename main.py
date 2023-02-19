import mpmath as mp
import matplotlib.pyplot as plt
import numpy as np
mp.mp.dps = 50  # number of decimal places used during computation


def g(x, a):
    return (x*(mp.psi(0, (x+1)/2) - mp.psi(0, x/2)) - a)/2


def p(x, a):
    return 1 - g(x, a)*mp.sin(mp.pi*x)/(mp.pi*x)


def luschny_factorial(x, a):
    return mp.gamma(x+1)*p(x, a)


def i(a):
    def integrand(x):
        return 1/luschny_factorial(x, a)
    return mp.quad(integrand, (0, mp.inf))


A = np.linspace(1, 5, 50)

y = [i(a) for a in A]

plt.plot(A, y)
plt.xlabel(r"$\alpha$")
plt.ylabel(r"$I(\alpha)$")
plt.savefig("Luschny_parameter.pdf")
