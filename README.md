# BIT 2118 Scientific Computing

This project contains Python examples for the BIT 2118 Scientific Computing
course. The programs demonstrate numerical methods from NumPy, SciPy, and
Matplotlib using practical engineering, computing, and data-analysis
examples.

## Project contents

The project includes Tasks 2–20:

| Task | Topic | Program |
| --- | --- | --- |
| 2 | NumPy arrays and numerical computation | [Task_02_numpy_arrays.py](./Task_02_numpy_arrays.py) |
| 3 | Mathematical functions and vectorization | [Task_03_vectorization.py](./Task_03_vectorization.py) |
| 4 | Floating-point arithmetic and numerical errors | [Task_04_numerical_errors.py](./Task_04_numerical_errors.py) |
| 5 | Matrix algebra and matrix operations | [Task_05_matrix_algebra.py](./Task_05_matrix_algebra.py) |
| 6 | Systems of linear equations | [Task_06_linear_systems.py](./Task_06_linear_systems.py) |
| 7 | Gaussian elimination and LU decomposition | [Task_07_lu_decomposition.py](./Task_07_lu_decomposition.py) |
| 8 | Iterative methods for linear systems | [Task_08_iterative_linear.py](./Task_08_iterative_linear.py) |
| 9 | Eigenvalues and eigenvectors | [Task_09_eigenvalues.py](./Task_09_eigenvalues.py) |
| 10 | Bisection and fixed-point methods | [Task_10_bisection_fixed_point.py](./Task_10_bisection_fixed_point.py) |
| 11 | Newton-Raphson and secant methods | [Task_11_newton_secant.py](./Task_11_newton_secant.py) |
| 12 | Polynomial and nonlinear equation solving | [Task_12_nonlinear_equations.py](./Task_12_nonlinear_equations.py) |
| 13 | Interpolation | [Task_13_interpolation.py](./Task_13_interpolation.py) |
| 14 | Curve fitting and approximation | [Task_14_curve_fitting.py](./Task_14_curve_fitting.py) |
| 15 | Numerical differentiation | [Task_15_numerical_differentiation.py](./Task_15_numerical_differentiation.py) |
| 16 | Numerical integration | [Task_16_numerical_integration.py](./Task_16_numerical_integration.py) |
| 17 | ODEs using the Euler method | [Task_17_euler_ode.py](./Task_17_euler_ode.py) |
| 18 | Numerical ODE solution using SciPy | [Task_18_scipy_ode.py](./Task_18_scipy_ode.py) |
| 19 | Numerical optimization | [Task_19_optimization.py](./Task_19_optimization.py) |
| 20 | Random numbers and Monte Carlo methods | [Task_20_monte_carlo.py](./Task_20_monte_carlo.py) |

## Requirements

- Python 3.10 or newer
- NumPy
- SciPy
- Matplotlib

The required packages are listed in
[requirements.txt](./requirements.txt).

## Installation

Open PowerShell in this project directory and run:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If `python` is not available, use the Windows Python launcher:

```powershell
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

To confirm that the packages are installed:

```powershell
python -c "import numpy, scipy, matplotlib; print(numpy.__version__, scipy.__version__, matplotlib.__version__)"
```

## Running a task

From the project directory, run an individual program with:

```powershell
python Task_16_numerical_integration.py
```

Tasks that use Matplotlib open a graph window. Close the graph window when
you have finished viewing it.

To check the syntax of every task without running the programs:

```powershell
python -m compileall .
```

To run all task files:

```powershell
Get-ChildItem -Filter "Task_*.py" | Sort-Object Name | ForEach-Object {
    Write-Host "`n===== $($_.Name) ====="
    python $_.FullName
}
```

## Task summaries

### Tasks 2–5: NumPy and numerical computation

- **Task 2:** Generates 30 random Celsius temperatures uniformly between
  -10 and 40, then calculates their mean, minimum, maximum, and Fahrenheit
  conversions. The sample changes on each run.
- **Task 3:** Compares a Python loop with NumPy vectorization for processing
  network-latency measurements. In the reported experiment with 1,000,000
  values, the loop took about 0.3329 seconds and the vectorized operation
  about 0.0080 seconds, making vectorization approximately 41.8 times faster.
  With only 10 values, the loop appeared faster because NumPy's setup and
  processing overhead can outweigh its benefits for very small inputs.
  Overall, vectorization is generally more efficient for large numerical
  datasets, while loops can suit small datasets or more complex
  item-by-item logic. The best choice depends on the data size and operation;
  timings vary by machine. The current script uses seed 100 to generate 10
  measurements.

#### Task 4: Numerical Precision, Error Analysis and Numerical Stability

##### 1. Floating-Point Precision

The experiment initially used 0.1 + 0.2 and compared the calculated result
with the expected value of 0.3. Additional test cases using different decimal
combinations, including 0.5 + 0.5, 0.25 + 0.25 and 0.123456789 + 0.987654321,
were introduced to observe how floating-point calculations behave with
different inputs.

**Conclusion:** The results demonstrated that computers do not always
represent decimal numbers with perfect accuracy. Some calculations produced
slight differences between the calculated and expected values, causing exact
comparisons to return False. However, tolerance-based comparisons using
`np.isclose()` were able to recognize that the values were sufficiently
close. This showed why tolerance-based comparisons are often more reliable
when working with floating-point numbers.

##### 2. Absolute Error and Relative Error

The experiment used the square root of 2 as the true value and compared it
against different approximations, ranging from 1.414213562 to 0.5. This
helped investigate how changing the accuracy of an approximation affects the
resulting errors.

**Conclusion:** The results showed that the further an approximation moves
away from the true value, the greater the absolute and relative errors
become. Highly accurate approximations produced very small errors, while
less accurate estimates resulted in larger differences. This demonstrated
that absolute error measures the actual difference between two values,
whereas relative error indicates how significant that difference is in
relation to the true value.

##### 3. Numerical Stability and Catastrophic Cancellation

The experiment compared two mathematically equivalent expressions using
different input values ranging from 1e-1 to 1e-16. The objective was to
investigate whether both expressions would maintain the same accuracy as the
input values became increasingly smaller.

**Conclusion:** The results showed that both expressions produced nearly
identical results when larger input values were used. However, as the inputs
approached zero, the direct expression started losing numerical precision
due to catastrophic cancellation, which occurs when subtracting two nearly
equal numbers. The stable expression avoided this subtraction and maintained
a result closer to the expected value of 0.5. At extremely small inputs, such
as 1e-16, the direct expression could even produce zero because of the
limitations of floating-point precision.

##### Overall Conclusion

Through these experiments, I developed a better understanding of how
numerical precision affects mathematical calculations performed by
computers. I observed that floating-point representation can introduce small
inaccuracies, making tolerance-based comparisons more appropriate than
relying entirely on exact equality. I also learned how absolute and relative
errors help measure the accuracy of numerical approximations and how
numerical stability affects the reliability of mathematical calculations.

The most important observation was that mathematically equivalent
expressions do not necessarily produce equally accurate computational
results. Choosing a numerically stable expression can significantly reduce
precision loss, particularly when working with extremely small values.
Overall, these experiments demonstrated the importance of understanding
floating-point limitations, measuring computational errors and selecting
appropriate mathematical approaches to achieve more reliable numerical
results.

### Matrix Transformations and Determinants

This experiment demonstrated how matrix transformations can be used to
rotate and scale points in a two-dimensional coordinate system. By changing
the rotation angle from 45° to 60°, I observed how the positions and
orientation of the transformed points changed. However, the determinant
remained theoretically constant at 3 because rotation does not affect the
area of a shape, while scaling by factors of 2 and 1.5 increases its area by
a factor of 3. Any extremely small variations in the calculated determinant
can be attributed to floating-point numerical precision. Overall, the
experiment helped me understand how matrix multiplication combines
different transformations and how determinants provide information about
the effect of a transformation on the area of geometric shapes.

### Tasks 6–9: Linear algebra

- **Task 6:** Solves a system of linear equations using `numpy.linalg.solve`.
- **Task 7:** Factors a matrix into permutation, lower-triangular, and
  upper-triangular matrices, then solves the system.
- **Task 8:** Compares Jacobi and Gauss-Seidel iterative methods with a
  direct solution.
- **Task 9:** Calculates the dominant eigenvalue and eigenvector of a
  network adjacency matrix to estimate node importance.

### Tasks 10–15: Equation solving and approximation

- **Task 10:** Finds a heat-balance equilibrium using bisection and
  fixed-point iteration.
- **Task 11:** Calculates an investment rate using Newton-Raphson and the
  secant method.
- **Task 12:** Solves a pair of nonlinear equations.
- **Task 13:** Estimates intermediate temperature values using linear
  interpolation and cubic splines.
- **Task 14:** Fits a quadratic model to server response-time data.
- **Task 15:** Estimates speed from GPS position measurements using finite
  differences.

### Tasks 16–20: Calculus, differential equations, and simulation

- **Task 16:** Estimates electrical energy consumption with the trapezoidal
  and Simpson rules.
- **Task 17:** Models Newton's law of cooling with the Euler method and
  compares it with the exact solution.
- **Task 18:** Models an RC charging circuit with `scipy.integrate.solve_ivp`
  and compares it with the exact curve.
- **Task 19:** Finds a low-cost allocation of two server types subject to a
  capacity constraint, including an integer comparison.
- **Task 20:** Estimates the probability of server overload with normally
  distributed demand scenarios and shows convergence.

## Assignment documentation requirements

For every task, document the following:

1. **Input values:** identify the data and parameters used.
2. **Mathematical operation:** state the numerical method or formula.
3. **Parameter change:** change at least one input or parameter and record
   how the result changes.
4. **Output interpretation:** explain the result in words and interpret any
   graph.
5. **Related real-world case:** modify the program to solve a different but
   related problem. State the new assumptions, input data, output, and
   interpretation.

Suggested parameter changes include:

- Change the temperature range or sample size in Task 2.
- Change the matrix or right-hand side in Tasks 6–9.
- Change the initial guess or tolerance in Tasks 10–12.
- Change the interpolation interval or measured values in Task 13.
- Add or modify response-time measurements in Task 14.
- Change the numerical step size in Tasks 15–18.
- Change the required capacity in Task 19.
- Change the random seed, demand distribution, or number of simulations
  in Task 20.

## Suggested related applications

- Analyze humidity readings instead of temperatures.
- Transform coordinates for a robot arm or camera.
- Model temperatures in a building rather than a single cooling object.
- Estimate vehicle distance from speed measurements.
- Optimize warehouse capacity or cloud-resource allocation.
- Estimate network-failure probability instead of server-overload risk.
