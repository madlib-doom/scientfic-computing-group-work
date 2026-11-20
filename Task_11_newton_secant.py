from scipy.optimize import root_scalar


cash_flows = [-200000, 6700000, 3500050, 400000, 256700]


def npv(rate: float) -> float:
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))


def d_npv(rate: float) -> float:
    return sum(
        -t * cf / (1 + rate) ** (t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )


newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.1,
    method="newton",
)
secant = root_scalar(npv, x0=0.05, x1=0.2, method="secant")

print(f"Newton-Raphson rate: {newton.root:.6%}")
print(f"Secant rate: {secant.root:.6%}")
