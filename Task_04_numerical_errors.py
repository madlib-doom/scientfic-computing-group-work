import numpy as np


test_cases = [
    (0.1, 0.2, 0.3),
    (0.5, 0.5, 1.0),
    (0.25, 0.25, 0.5),
    (0.123456789, 0.987654321, 1.111111110)
]

for a, b, expected in test_cases:

    calculated = a + b

    print(f"\n{a} + {b}")
    print(f"Calculated: {calculated:.20f}")
    print(f"Expected:   {expected:.20f}")
    print(f"Exact comparison: {calculated == expected}")
    print(f"Tolerance comparison: {np.isclose(calculated, expected)}")

true_value = np.sqrt(2)
approximations = [
    1.414213562,
    1.414,
    1.4,
    1.0,
    0.5
]

for approx_value in approximations:

    absolute_error = abs(true_value - approx_value)
    relative_error = absolute_error / abs(true_value)

    print(f"\nApproximation: {approx_value}")
    print(f"Absolute error: {absolute_error:.8f}")
    print(f"Relative error: {relative_error:.8%}")

values = [
    1e-1,
    1e-2,
    1e-4,
    1e-8,
    1e-12,
    1e-14,
    1e-16
]

for x in values:

    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)

    difference = abs(direct - stable)

    print(f"\nx = {x:.0e}")
    print(f"Direct result: {direct:.12f}")
    print(f"Stable result: {stable:.12f}")
    print(f"Difference:    {difference:.12e}")