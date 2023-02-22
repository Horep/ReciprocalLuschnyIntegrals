import mpmath as mp
mp.mp.dps = 400  # number of decimal places used during computation


def g(x):
    return (x*(mp.psi(0, (x+1)/2) - mp.psi(0, x/2)) - 1)/2


def p(x):
    return 1 - g(x)*mp.sin(mp.pi*x)/(mp.pi*x)


def recip_luschny_factorial(x):
    return 1/(mp.gamma(x+1)*p(x))


def give_digits():
    return mp.quad(recip_luschny_factorial, (0, mp.inf))

print(give_digits())
