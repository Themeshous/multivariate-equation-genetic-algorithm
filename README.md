# multivariate-equation-genetic-algorithm
## Solving an equation with several variables using the concept of genetic algorithm:
We want to solve the following problem, a+2b+3c+4d = 30. For this, a general algorithm will be used to find the value of a, b, c and d that satisfies the problem.
will be used to find the value of a, b, c and d that satisfies the above equation.
First, we should formulate the objective function of this problem, the objective is to minimize the value of the function f(x)
value of the function f(x) where f(x) = ((a + 2b + 3c + 4d) - 30). To speed up the calculation, we limit ourselves to the use of integer variables.
to use integer variables between 0 and 30 for our searched variables a, b, c and d.
The chromosome is thus defined as: a-b-c-d.
Example:
We define the number of chromosomes in the population by 6 for example, then we will generate a random value of the genes.
random value of the genes "a, b, c, d" for the 6 chromosomes.
We fix an objective function for each chromosome produced during the initialization step and we apply the steps of the
and we apply the steps of the genetic algorithm.
