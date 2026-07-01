from math import exp, log

R = 8.314462618  # J mol^-1 K^-1

def arrhenius(A, Ea, T):
    return A * exp(-Ea / (R * T))

def zero_order(c0, k, t):
    return max(c0 - k * t, 0.0)

def first_order(c0, k, t):
    return c0 * exp(-k * t)

def second_order(c0, k, t):
    return c0 / (1 + k * c0 * t)

def half_life_first(k):
    return log(2.0) / k

def rate_constant_ratio(Ea, T1, T2):
    """k(T2)/k(T1) from the two-temperature Arrhenius form."""
    return exp(-Ea / R * (1.0 / T2 - 1.0 / T1))
